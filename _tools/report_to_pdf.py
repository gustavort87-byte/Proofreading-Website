"""Render a proofreading REPORT.md as a styled PDF next to it (REPORT.pdf).

Usage:  python -I report_to_pdf.py [--footer "Label"] <path/to/REPORT.md> [more REPORT.md ...]

Handles the Markdown subset the reports use: #/##/### headings, paragraphs,
"-" and "1." lists (two-space nesting), pipe tables, **bold**, `code`, [links](url).
Landscape Letter so the findings table stays readable.
"""
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (ListFlowable, ListItem, Paragraph,
                                SimpleDocTemplate, Spacer, Table, TableStyle)

FONTS = Path("C:/Windows/Fonts")
pdfmetrics.registerFont(TTFont("Arial", str(FONTS / "arial.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Bold", str(FONTS / "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Italic", str(FONTS / "ariali.ttf")))
pdfmetrics.registerFont(TTFont("Consolas", str(FONTS / "consola.ttf")))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold",
                              italic="Arial-Italic", boldItalic="Arial-Bold")

NAVY = colors.HexColor("#1F3D5C")
TEAL = colors.HexColor("#2C8282")
LIGHT = colors.HexColor("#F3FAFA")
GRID = colors.HexColor("#C9D6DF")
SEVERITY = {
    "critical": colors.HexColor("#B42318"),
    "high": colors.HexColor("#C4320A"),
    "medium": colors.HexColor("#8A6100"),
    "low": colors.HexColor("#475467"),
}

BASE = ParagraphStyle("base", fontName="Arial", fontSize=9.5, leading=13, alignment=TA_LEFT)
STYLES = {
    "h1": ParagraphStyle("h1", parent=BASE, fontName="Arial-Bold", fontSize=18, leading=22,
                         textColor=NAVY, spaceAfter=8),
    "h2": ParagraphStyle("h2", parent=BASE, fontName="Arial-Bold", fontSize=13.5, leading=17,
                         textColor=NAVY, spaceBefore=12, spaceAfter=6),
    "h3": ParagraphStyle("h3", parent=BASE, fontName="Arial-Bold", fontSize=11, leading=14,
                         textColor=TEAL, spaceBefore=8, spaceAfter=4),
    "p": ParagraphStyle("p", parent=BASE, spaceAfter=6),
    "li": ParagraphStyle("li", parent=BASE, spaceAfter=2),
    "cell": ParagraphStyle("cell", parent=BASE, fontSize=8, leading=10.2),
    "head": ParagraphStyle("head", parent=BASE, fontName="Arial-Bold", fontSize=8.2,
                           leading=10.2, textColor=colors.white),
}


def inline(text):
    """Escape for reportlab and convert inline Markdown to its mini-markup."""
    parts = re.split(r"(`[^`]*`)", text)
    out = []
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) > 1:
            code = part[1:-1].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            out.append(f'<font name="Consolas" color="#1F3D5C">{code}</font>')
            continue
        part = part.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        part = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", part)
        part = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<link href="\2" color="#2C8282">\1</link>', part)
        out.append(part)
    return "".join(out)


def split_row(line):
    cells, buf, in_code = [], "", False
    for ch in line.strip().strip("|"):
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append(buf.strip())
            buf = ""
        else:
            buf += ch
    cells.append(buf.strip())
    return cells


def col_widths(rows, total):
    """Each column gets at least its longest word (so nothing breaks mid-word),
    then the remaining width is shared by typical text length."""
    n = len(rows[0])
    mins, weights = [], []
    for c in range(n):
        col = [r[c] if c < len(r) else "" for r in rows]
        words = [w for cell in col for w in re.sub(r"[*`\[\]]", "", cell).split()]
        longest = max((pdfmetrics.stringWidth(w, "Arial-Bold", 8.2) for w in words), default=10)
        mins.append(min(longest + 10, total * 0.12))  # long paths may still wrap
        lengths = sorted(len(x) for x in col)
        typical = lengths[int(len(lengths) * 0.8)]
        weights.append(max(4, min(typical, 120)) ** 0.85)
    spare = max(0, total - sum(mins))
    s = sum(weights)
    return [m + spare * w / s for m, w in zip(mins, weights)]


def make_table(rows, width):
    has_header = any(rows[0])
    body = rows[1:]  # an all-empty header row ("| | |") is dropped, not drawn
    widths = col_widths(rows if has_header else body, width)
    data = []
    if has_header:
        data.append([Paragraph(inline(c), STYLES["head"]) for c in rows[0]])
    sev_col = next((i for i, c in enumerate(rows[0]) if c.lower() == "severity"), None)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.4, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    if has_header:
        style += [("BACKGROUND", (0, 0), (-1, 0), NAVY)]
    offset = 1 if has_header else 0
    for r, row in enumerate(body):
        row = row + [""] * (len(widths) - len(row))
        cells = []
        for c, val in enumerate(row[:len(widths)]):
            txt = inline(val)
            if c == sev_col and val.lower() in SEVERITY:
                txt = f'<font color="{SEVERITY[val.lower()].hexval()}"><b>{txt}</b></font>'
            if not has_header and c == 0:
                txt = f"<b>{txt}</b>"
            cells.append(Paragraph(txt, STYLES["cell"]))
        data.append(cells)
        if r % 2 == 1:
            style.append(("BACKGROUND", (0, r + offset), (-1, r + offset), LIGHT))
    t = Table(data, colWidths=widths, repeatRows=1 if has_header else 0)
    t.setStyle(TableStyle(style))
    return t


def make_list(items):
    """items: list of (indent_level, ordered, text). Builds nested ListFlowables."""
    def build(i, level):
        flow, ordered = [], items[i][1]
        while i < len(items) and items[i][0] >= level:
            lvl, _, text = items[i]
            if lvl > level:
                sub, i = build(i, lvl)
                flow[-1].append(sub)
                continue
            flow.append([Paragraph(inline(text), STYLES["li"])])
            i += 1
        lf = ListFlowable([ListItem(x) for x in flow],
                          bulletType="1" if ordered else "bullet",
                          start="1" if ordered else "•", leftIndent=14 + 4 * level,
                          bulletFontName="Arial", bulletFontSize=8, bulletColor=TEAL)
        return lf, i
    lf, _ = build(0, items[0][0])
    return lf


def convert(md_path, footer="The Spanish Group · Proofreading"):
    md_path = Path(md_path)
    lines = md_path.read_text(encoding="utf-8").splitlines()
    pdf_path = md_path.with_suffix(".pdf")
    page = landscape(letter)
    margin = 0.5 * inch
    width = page[0] - 2 * margin
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), md_path.stem)

    story, para, i = [], [], 0

    def flush():
        if para:
            story.append(Paragraph(inline(" ".join(para)), STYLES["p"]))
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            flush(); i += 1; continue
        m = re.match(r"^(#{1,3})\s+(.*)", line)
        if m:
            flush()
            story.append(Paragraph(inline(m.group(2)), STYLES["h" + str(len(m.group(1)))]))
            i += 1; continue
        if s.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if not re.match(r"^\|?\s*:?-{3,}", lines[i].strip()):
                    rows.append(split_row(lines[i]))
                i += 1
            story += [make_table(rows, width), Spacer(1, 8)]
            continue
        lm = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", line)
        if lm:
            flush()
            items = []
            while i < len(lines):
                lm = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", lines[i])
                if lm:
                    items.append([len(lm.group(1)) // 2, lm.group(2)[0].isdigit(), lm.group(3)])
                elif lines[i].strip() and lines[i].startswith(" ") and items:
                    items[-1][2] += " " + lines[i].strip()   # wrapped continuation line
                else:
                    break
                i += 1
            story += [make_list(items), Spacer(1, 4)]
            continue
        para.append(s)
        i += 1
    flush()

    def decorate(canvas, doc):
        canvas.saveState()
        canvas.setFont("Arial", 7.5)
        canvas.setFillColor(colors.HexColor("#667085"))
        canvas.drawString(margin, 0.3 * inch, f"{footer} · {title}")
        canvas.drawRightString(page[0] - margin, 0.3 * inch, f"Page {doc.page}")
        canvas.setStrokeColor(TEAL)
        canvas.setLineWidth(1.2)
        canvas.line(margin, page[1] - 0.35 * inch, page[0] - margin, page[1] - 0.35 * inch)
        canvas.restoreState()

    doc = SimpleDocTemplate(str(pdf_path), pagesize=page, leftMargin=margin, rightMargin=margin,
                            topMargin=0.55 * inch, bottomMargin=0.5 * inch,
                            title=title, author=footer)
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
    return pdf_path


if __name__ == "__main__":
    args = sys.argv[1:]
    footer = {}
    if "--footer" in args:   # optional footer label for non-proofreading reports
        k = args.index("--footer")
        footer = {"footer": args[k + 1]}
        del args[k:k + 2]
    if not args:
        sys.exit(__doc__)
    for arg in args:
        print(convert(arg, **footer))
