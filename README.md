# Proofreading workflow — The Spanish Group / Certified Translations

**Shareable site:** https://gustavort87-byte.github.io/Proofreading-Website/ (GitHub Pages, `gh-pages`
branch, built by `_tools/build_site.py`, published with `bash _tools/publish.sh`; every page is `noindex`).

Trigger: the user shares a URL on thespanishgroup.org (or a TSG / Certified Translations page).
Output for each URL: the findings report (`REPORT.md` + its PDF, `REPORT.pdf`) and the corrected
`proofread.html`, plus an INDEX row.

## Reference (built once, refresh only on request)

- `_reference/home-template.html` — raw HTML of https://thespanishgroup.org (HOME), 2026-10-22.
- `_reference/style-guide.md` — tone, sections, typography, palette, CTAs, copy rules, brand-term
  dictionary, known HOME issues. Read before every audit.
- `_tools/report_to_pdf.py` — converts a `REPORT.md` into `REPORT.pdf` (reportlab).
- `_tools/build_site.py`, `_tools/publish.sh` — build and publish the GitHub Pages site.
- `_reference/branding.json`, `_reference/metadata.json` — Firecrawl branding/metadata output.

## Steps per URL

1. Strip tracking parameters. Check `INDEX.md`: if the URL was audited before, this run gets a
   "Vs. previous audit" section.
2. Scrape with Firecrawl: `formats: ["rawHtml"]`, `maxAge: 0`. Large results land in
   `tool-results/`; parse them with `python -I`, never read them whole.
3. Create `Proofreading/<YYYY-MM-DD>_<url-slug>/`. Save the capture as `original.html` (needed to
   diff and to prove every change).
4. Audit by category: grammar/spelling (page language), copy & tone vs. style guide (no
   placeholders), design vs. HOME (colors, type, spacing, hierarchy), buttons & CTAs (label,
   placement, contrast, every href checked), responsive (375 / 768 / 1440 from CSS and markup),
   Windows/Mac compatibility (risky CSS, unloaded fonts, vendor prefixes), on-page SEO and basic
   accessibility (title, meta description, H1, heading order, alt text, WCAG AA contrast).
   Verify hrefs by scraping each unique internal destination (`formats: ["links"]` or a cheap
   scrape; watch the ~10 req/min limit) or say which were not checked.
   Take full-page screenshots at 375 / 768 / 1440 into `screenshots/` (3 credits) and view them in slices.
   Location landing pages are also checked against the approved standard in
   `C:/Users/carlo/Agentic Workflows/TSG Landing Page/LANDING_PAGE_STANDARD.md`.
5. Write `proofread.html`: copy of `original.html` with only the fixes listed in the report.
   Make relative asset URLs absolute (or add `<base href>`) so it renders locally with original
   styles. Do not recolor brand elements site-wide (see style guide section 4).
6. Write `REPORT.md`:
   - Audited URL, date, capture time, cache state
   - Overall score + per-category score (1-10)
   - Findings table: # | Category | Severity | Location | Issue | Fix applied
   - Comparison vs. HOME template
   - Changes applied to HTML (Before → After, grouped by section) — must match the diff exactly
   - Not verifiable via scraping
   - Vs. previous audit (re-audits only)
7. Diff `original.html` vs `proofread.html` and confirm every hunk appears under "Changes applied"
   and nothing else changed.
8. Render the PDF: `python -I Proofreading/_tools/report_to_pdf.py Proofreading/<folder>/REPORT.md`
   (writes `REPORT.pdf` beside it; landscape Letter, Arial). Rasterize a few pages with `pypdfium2`
   and look at them before delivering. If the report is edited later, re-run the script so the PDF
   never drifts from the Markdown.
9. Append the row to `INDEX.md`.
10. Publish: commit the new audit folder and `INDEX.md` on `main`, push, then run
    `bash _tools/publish.sh` (rebuilds `_site/`, pushes `gh-pages`). Reply with folder, score,
    top 3 findings, the PDF path and the shareable link
    `https://gustavort87-byte.github.io/Proofreading-Website/audits/<folder>/report.html`.

## Rules

- No invented findings. Unverifiable items go in their own section, not the table.
- Report in English; HTML copy stays in the page's language.
- Never alter terms in the style guide's brand-term dictionary.
- Never invent testimonials, statistics or trust claims.
