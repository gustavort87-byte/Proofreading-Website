"""Build the shareable GitHub Pages site for the proofreading audits into _site/.

Usage (from Proofreading/):  python -I _tools/build_site.py

Reads INDEX.md for the list of audits, copies each audit folder, renders REPORT.md
as report.html, adds a side-by-side compare.html, and injects noindex into every
published HTML page (the copies only; the audit folders stay untouched).
"""
import html
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
NOINDEX = '<meta name="robots" content="noindex, nofollow">'

CSS = """
:root{--navy:#1F3D5C;--teal:#2C8282;--teal-l:#47ACAD;--bg:#F6F8FA;--line:#D6E0E6;--text:#1D2939;--muted:#667085}
*{box-sizing:border-box}body{margin:0;font-family:Lato,system-ui,-apple-system,"Segoe UI",Arial,sans-serif;color:var(--text);background:var(--bg);line-height:1.5}
header.top{background:var(--navy);color:#fff;padding:20px 16px}header.top .wrap{display:flex;flex-wrap:wrap;gap:8px 24px;align-items:baseline}
header.top h1{margin:0;font-size:22px}header.top p{margin:0;color:#C9D6DF;font-size:14px}header.top a{color:#fff}
.wrap{max-width:1180px;margin:0 auto;padding:0 16px}main.wrap{padding-top:24px;padding-bottom:48px}
.card{background:#fff;border:1px solid var(--line);border-radius:10px;padding:18px 20px;margin-bottom:16px}
.card h2{margin:0 0 4px;font-size:18px;color:var(--navy)}.card .url{font-size:13px;color:var(--muted);word-break:break-all}
.stats{display:flex;gap:12px;flex-wrap:wrap;margin:12px 0}.stat{border:1px solid var(--line);border-radius:8px;padding:6px 12px;font-size:13px}
.stat b{font-size:18px;color:var(--navy);display:block}.stat.crit b{color:#B42318}
.btns{display:flex;flex-wrap:wrap;gap:8px}.btn{display:inline-block;padding:8px 14px;border-radius:999px;background:var(--teal);color:#fff;text-decoration:none;font-size:14px;font-weight:700}
.btn.ghost{background:#fff;color:var(--teal);border:1px solid var(--teal)}.btn:hover{filter:brightness(1.08)}
.report{background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 24px 24px;overflow-wrap:anywhere}
.report h1{color:var(--navy);font-size:26px}.report h2{color:var(--navy);border-bottom:2px solid var(--teal-l);padding-bottom:4px;margin-top:32px}
.report h3{color:var(--teal)}.report code{font-family:Consolas,Menlo,monospace;font-size:.88em;background:#EEF4F6;padding:1px 4px;border-radius:4px;color:var(--navy)}
.tablewrap{overflow-x:auto;margin:12px 0}.report table{border-collapse:collapse;width:100%;font-size:13.5px}
.report th{background:var(--navy);color:#fff;text-align:left;padding:7px 8px;position:sticky;top:0}
.report td{border:1px solid var(--line);padding:6px 8px;vertical-align:top}.report tr:nth-child(even) td{background:#F3FAFA}
.sev-critical{color:#B42318;font-weight:700}.sev-high{color:#C4320A;font-weight:700}.sev-medium{color:#8A6100;font-weight:700}.sev-low{color:#475467;font-weight:700}
.shots{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}.shots a{display:block;background:#fff;border:1px solid var(--line);border-radius:8px;padding:8px;text-decoration:none;color:var(--navy);font-size:14px}
.shots img{width:100%;height:220px;object-fit:cover;object-position:top;border-radius:4px;display:block;margin-bottom:6px}
footer{color:var(--muted);font-size:12px;text-align:center;padding:24px 16px}
"""


def page(title, body, extra_head=""):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
{NOINDEX}<title>{html.escape(title)}</title><style>{CSS}</style>{extra_head}</head>
<body>{body}<footer>The Spanish Group · Proofreading audits · internal review copy, not the live site</footer></body></html>
"""


def read_index():
    rows = []
    for line in (ROOT / "INDEX.md").read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 5 and re.match(r"\d{4}-\d{2}-\d{2}$", cells[0]):
            folder = re.search(r"\(([^)]+?)/?\)", cells[2]).group(1)
            rows.append({"date": cells[0], "url": cells[1], "folder": folder,
                         "score": cells[3], "critical": cells[4]})
    return rows


def noindex(path):
    """Swap any robots meta for noindex, or add one after <head>."""
    text = path.read_text(encoding="utf-8")
    text, n = re.subn(r'<meta name="robots" content="[^"]*">', NOINDEX, text)
    if not n:
        text = re.sub(r"<head([^>]*)>", lambda m: m.group(0) + NOINDEX, text, count=1)
    path.write_text(text, encoding="utf-8", newline="")


def report_html(md_text, a):
    body = markdown.markdown(md_text, extensions=["tables", "sane_lists"])
    body = body.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
    body = re.sub(r"<td>(Critical|High|Medium|Low)</td>",
                  lambda m: f'<td class="sev-{m.group(1).lower()}">{m.group(1)}</td>', body)
    title = re.search(r"<h1>(.*?)</h1>", body)
    title = re.sub("<[^>]+>", "", title.group(1)) if title else a["folder"]
    top = f"""<header class="top"><div class="wrap"><h1>{title}</h1>
<p><a href="../../">← All audits</a></p></div></header>
<main class="wrap"><div class="card"><div class="btns">
<a class="btn" href="REPORT.pdf">Download PDF</a>
<a class="btn ghost" href="compare.html">Compare original vs corrected</a>
<a class="btn ghost" href="proofread.html">Corrected page</a>
<a class="btn ghost" href="original.html">Original page</a>
<a class="btn ghost" href="REPORT.md">Markdown</a></div>
<p style="margin:12px 0 0;font-size:13px;color:var(--muted)">The original and corrected pages are rendered from the HTML captured on the audit date. They load images and styles from the dev site, and a few live-site style rules (such as link underlines) may look slightly different here. Every content change is listed in the report.</p></div>
{shots_block(a)}<article class="report">{body}</article></main>"""
    return page(title, top)


def shots_block(a):
    shots = sorted((OUT / "audits" / a["folder"] / "screenshots").glob("*.png"))
    if not shots:
        return ""
    items = "".join(f'<a href="screenshots/{s.name}"><img src="screenshots/{s.name}" alt="Screenshot {s.stem}" loading="lazy">{s.stem}</a>'
                    for s in shots)
    return f'<div class="card"><h2>Screenshots (original page)</h2><div class="shots">{items}</div></div>'


COMPARE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
{noindex}<title>Compare · {folder}</title><style>
body{{margin:0;font-family:Lato,system-ui,Arial,sans-serif;background:#1F3D5C;color:#fff}}
.bar{{display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:10px 16px}}.bar a{{color:#fff}}
.bar button{{border:1px solid #47ACAD;background:transparent;color:#fff;border-radius:999px;padding:6px 12px;cursor:pointer}}
.bar button.on{{background:#47ACAD}}.panes{{display:flex;gap:12px;padding:0 12px 12px;overflow-x:auto}}
.pane{{flex:0 0 auto}}.pane h2{{font-size:14px;margin:4px 0 6px}}iframe{{border:0;background:#fff;border-radius:6px}}
</style></head><body>
<div class="bar"><a href="report.html">← Report</a><span>Width:</span>
<button data-w="375">375</button><button data-w="768">768</button><button data-w="1440" class="on">1440</button>
<span style="opacity:.8;font-size:13px">Scroll each pane independently. Both panes render the captured HTML, so small styling details (e.g. link underlines) can differ from the live site in the same way on both sides.</span></div>
<div class="panes"><div class="pane"><h2>Original</h2><iframe src="original.html" title="Original page"></iframe></div>
<div class="pane"><h2>Corrected</h2><iframe src="proofread.html" title="Corrected page"></iframe></div></div>
<script>
const fr=[...document.querySelectorAll('iframe')];
function set(w){{const fit=Math.max(320,(innerWidth-48)/2),z=w>fit?fit/w:1;fr.forEach(f=>{{f.style.width=w+'px';f.style.height=((innerHeight-110)/z)+'px';f.parentElement.style.zoom=z}});
document.querySelectorAll('button').forEach(b=>b.classList.toggle('on',+b.dataset.w===w))}}
document.querySelectorAll('button').forEach(b=>b.onclick=()=>set(+b.dataset.w));set(1440);addEventListener('resize',()=>set(+document.querySelector('button.on').dataset.w));
</script></body></html>
"""


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    audits = read_index()
    cards = []
    for a in audits:
        src, dst = ROOT / a["folder"], OUT / "audits" / a["folder"]
        shutil.copytree(src, dst)
        for name in ("original.html", "proofread.html"):
            if (dst / name).exists():
                noindex(dst / name)
        md = (src / "REPORT.md").read_text(encoding="utf-8")
        (dst / "report.html").write_text(report_html(md, a), encoding="utf-8")
        (dst / "compare.html").write_text(COMPARE.format(noindex=NOINDEX, folder=html.escape(a["folder"])), encoding="utf-8")
        title = re.search(r"^# (.+)$", md, re.M)
        cards.append(f"""<div class="card"><h2>{html.escape(title.group(1) if title else a['folder'])}</h2>
<div class="url">{html.escape(a['url'])} · audited {a['date']}</div>
<div class="stats"><div class="stat"><b>{a['score']}</b>score / 10</div><div class="stat crit"><b>{a['critical']}</b>critical</div></div>
<div class="btns"><a class="btn" href="audits/{a['folder']}/report.html">Open report</a>
<a class="btn ghost" href="audits/{a['folder']}/REPORT.pdf">PDF</a>
<a class="btn ghost" href="audits/{a['folder']}/compare.html">Compare</a>
<a class="btn ghost" href="audits/{a['folder']}/proofread.html">Corrected page</a></div></div>""")
    body = f"""<header class="top"><div class="wrap"><h1>Proofreading audits</h1>
<p>The Spanish Group / Certified Translations · {len(audits)} audit(s)</p></div></header>
<main class="wrap">{''.join(reversed(cards))}</main>"""
    (OUT / "index.html").write_text(page("Proofreading audits", body), encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    print(f"Built {len(audits)} audit(s) into {OUT}")


if __name__ == "__main__":
    build()
