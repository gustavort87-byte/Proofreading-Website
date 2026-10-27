# The Spanish Group — Style Guide (derived from HOME)

Source: https://thespanishgroup.org/ captured 2026-10-22 with Firecrawl (`rawHtml` + `branding`, `maxAge: 0`,
live fetch, HTTP 200). Raw page: `home-template.html`. Stylesheets read: `new_landing_page.css` and
`style-custom.css` (WP Rocket minified cache), plus inline `<style>` blocks. Firecrawl's automatic
brand detection had low confidence (0.53 overall), so every value below was checked against the CSS.

Use this file as the yardstick for every audit. Where HOME itself breaks a rule, it is listed in
"Known issues on HOME" so the audit does not copy the mistake into other pages.

---

## 1. Brand tone

- **Voice:** professional, reassuring, plain-spoken, with a light, confident informality
  ("Yes, it's really that easy!", "Not false advertising, we promise.", "Because nobody likes
  surprises when it comes to pricing.").
- **Promise pillars** (repeat across pages, keep wording consistent):
  - Certified translations with **guaranteed acceptance**
  - **Speed:** same-day delivery available; documents under 9 pages generally in 1–2 business days;
    "receive your document in as little as 1 hour"
  - **Accuracy / quality control:** ISO 9001:2015 and ISO 17100:2015, ATA member
  - **Security:** "Military grade data and document security", "Absolute Document Confidentiality"
  - **Reach:** 120+ languages (see Known issues: some places still say 90)
  - **Support:** "Open 24/7 | Call Now: (800) 460-1536"
- **Person:** "we/our" for the company, "you/your" for the customer. Benefits first, then process.
- **Audience:** individuals (immigration, civil documents, academic) and organizations (legal,
  business, medical, website). Pages for one audience should not drift into the other's language.
- **Avoid:** exaggeration without proof, competitor mentions, legal guarantees beyond
  "guaranteed acceptance", invented reviews or statistics, placeholder text (Lorem ipsum, [City],
  TBD, XXX).

## 2. Section structure (HOME order)

| # | Section | Selector / class | Content pattern |
|---|---|---|---|
| 0 | Top bar + header nav | `#top-bar`, `#site-navigation`, `.menu` | Logo (white), Home / Certified Translation menu, pill buttons **Get Price** + **Order Translation**, **Track Order**, phone `(800) 460-1536`, language selector |
| 1 | Hero | `section.sectionHero` | H1 (with `.text-primary` teal span), one-sentence value prop, promo line, two CTAs **Order Translation** (primary) + **Get Free Quote** (outline), review avatars + stars + "98% of customers… 4 or 5-Star rating", hero image right, lead form (First Name, Email, **Get Started**), trust row (ATA logo, ISO 9001 / ISO 17100, Shopper Approved) |
| 2 | Process + Pricing | `section#rotatingPricing` | H2 "Effortless Process" + H6 step + paragraph; H2 "Simple Pricing" with three price cards; H2 "Efficient Service" + turnaround promise; CTA pair **Get Free Quote** / **Order Translation** |
| 3 | Languages / benefits | `section.flu_lang_sec` (dark blue bg) | H2 "We're Fluent in Over 120 languages", 4 check-mark bullets, CTA pair |
| 4 | Services grid | `.icon-services.homepage`, `.magic-box` | H2 "Certified Translation Solutions for our Clients' Diverse Needs"; H3 service + H4 one-line audience description + text link CTA (Document, Certified, Corporate, Legal, Transcript & Diploma, Website, Verify Your Price, Order Your Translation) |
| 5 | Feature boxes | `.box-pad` / `.box-pad1` | H2 + short paragraph + CTA: Confirm Pricing, Place An Order, FAQ (with phone), video, Become a Provider, 120+ Languages, Create an Account |
| 6 | SEO content | `#seo_section` | H2 "Comprehensive Translation Solutions" + long-form paragraph |
| 7 | Footer | `#footer` (bg `#15536E`, top-right radius 70px) | H2 "Let's Get Social" + social icons, phone, © year The Spanish Group LLC, privacy badge, H2 "Site Navigation" link lists, "Return to Top" |

The HOME template contains five language variants of most blocks (English, Spanish, Portuguese,
French, Chinese) toggled by classes `.spanish`, `.portuguese`, `.french`, `.chinese` (hidden by
default). Only the variant matching the page language is visible; audit that one, but check the
hidden variants for broken hrefs since they ship in the HTML.

## 3. Typography

| Role | Family (as declared) | Size / weight | Notes |
|---|---|---|---|
| Body | `'Lato', sans-serif` (self-hosted woff: 300, 400, 700) | `body` 20px; most components 16–18px | `* { font-family: 'Lato' }` |
| Headings + `p` | `'Roboto', sans-serif !important` (h1–h6, p) | Hero H1 56px / 64px line-height, bold, `text-wrap: balance`; 36px/42px on mobile. Section H2 40px, 800 (`.homepage-heading`), 32px ≤992px. `.flu_lang_sec h2` 44px, 900 | **Roboto is not loaded** (no `@font-face`, no Google Fonts link) — renders as the system sans-serif: Arial on Windows, Helvetica on macOS, Roboto on Android |
| Menu | `Aller, Helvetica, sans-serif !important` (more-menu), `'gothamBold'` (`.flu_lang_sec h2`) | 21px, 700 | Aller and Gotham are not loaded either → fallbacks |
| Buttons | Roboto (how-it-works), Lato elsewhere | 16–18px, 700 | |

Conventions: Title Case for H1–H3 and button labels; sentence case for H4 descriptions and body.

## 4. Color palette

| Token | Hex | Where used |
|---|---|---|
| Teal (primary brand, "green-tear") | `#47ACAD` | `.bg-green-tear`, CTA buttons, `.text-primary` highlight in H1, icons, legal alert bar |
| Teal dark (button base / hover) | `#2C8282` | Hero `.button` base, `ul.flu_lang_sec_btn_ul a:hover` |
| Teal alt (bullets / hover) | `#169F9B` | `.sky_blue`, check-mark icons, menu catalogue hover |
| Navy (secondary) | `#2B4763` | `.bg-dark-blue`, top bar, `flu_lang_sec` background, language options |
| Navy deep | `#1F3D5C` / `#203D5B` | Site navigation, more-menu, order status, mobile CTA bar, certified badge |
| Royal navy (quote button) | `#1B4775` | `#nfnQuoteBtn`, first `.how_it_works_btns` button |
| Footer blue | `#15536E` | `#footer` background |
| Menu hover blue | `#7094B8` | `.menu li a:hover` |
| Accent blue | `#398CED` | check icons in languages list, `.switch-candy` |
| Link blue (Bootstrap) | `#0D6EFD` | default links |
| Light blue panel | `#E1EFFF` | `.price_text`, `.box-pad` |
| Promo panel | `#F3FAFA` bg, `#173D5D` text, `#42AAAD` border | `.promo-option-3` |
| Text | `#212529` (Bootstrap body), `#000000` headings, `#5B5B5B` price copy, `#888888` labels | |
| Background | `#FFFFFF` | |

### Contrast (WCAG 2.1 AA: 4.5:1 normal text, 3:1 large ≥24px or ≥18.66px bold)

| Pair | Ratio | Verdict |
|---|---|---|
| White on `#47ACAD` (teal buttons) | 2.70 | **Fails** AA for all text sizes |
| `#47ACAD` on white (teal text / outline button) | 2.70 | **Fails** |
| White on `#169F9B` | 3.25 | Large text only |
| White on `#398CED` | 3.42 | Large text only |
| `#47ACAD` on `#2B4763` | 3.56 | Large text only |
| `#888888` on white | 3.54 | Large text only |
| White on `#2C8282` | 4.54 | Passes (barely) |
| White on `#2B4763` / `#1F3D5C` / `#1B4775` / `#15536E` | 9.6 / 11.2 / 9.5 / 8.4 | Passes |
| `#5B5B5B` on `#E1EFFF` | 5.82 | Passes |
| `#212529` on white | 15.43 | Passes |

Audit rule: a page that uses the same teal-on-white or white-on-teal combination as HOME gets the
finding logged (Medium, accessibility) but the color is **not** changed in `proofread.html` unless
the user asks, because it is a site-wide brand decision. Recommend `#2C8282` as the AA-safe teal.

## 5. Buttons and CTAs

- **Shape:** pill (`rounded-pill`, radius 30px+ / 800px); legacy blocks use 5–7px radius.
- **Primary:** teal fill (`#47ACAD` over `#2C8282`), white bold text, padding 10–14px × 20–22px.
  Hover: the `::before` overlay shrinks to reveal `#2C8282`.
- **Secondary / outline:** white fill, teal text and border; hover flips to teal fill + white text.
- **Dark variant:** `#1B4775` / `#203D5B` fill, white text (quote button in older blocks, mobile menu).
- **Pairing and order:** CTAs come in pairs, primary first:
  **Order Translation** (→ `/billing/`) + **Get Free Quote** (→ `/translations/quotes/`).
  Header uses **Get Price** + **Order Translation**; menus use **Get Instant Quote**.
- **Placement:** hero (above the fold), after process/pricing, in the languages band, at the end of
  each service card (text link), in feature boxes, and a fixed bottom bar on mobile (`.nfn__actions`).
- **Approved CTA labels and destinations (English):**

| Label | Destination |
|---|---|
| Order Translation / Order A Translation / Get Started / Place An Order | `https://thespanishgroup.org/billing/` |
| Get Free Quote / Get Instant Quote / Get Price / Verify Price / Confirm Pricing | `https://thespanishgroup.org/translations/quotes/` |
| Track Order | `https://thespanishgroup.org/?order-status=tracker` |
| Let's Answer Those Questions / FAQ | `https://thespanishgroup.org/translations/frequently-asked-questions/` |
| Contact us | `https://thespanishgroup.org/contact-us/` |
| Phone | `tel:8004601536`, displayed `(800) 460-1536` |

- **Spanish equivalents:** Cotización / Solicitar cotización → `/traducciones/cotizacion/`;
  Ordenar traducción → `/pedidos/`; Preguntas frecuentes → `/traducciones/preguntas-frecuentes/`.
- Every `href` must be absolute `https://thespanishgroup.org/...`, resolve with 200, and match its
  label. No `#`, `javascript:`, `None`, or staging (`devsite.`) hosts on production pages.

## 6. Copy conventions

- **Language:** US English (`lang="en"`), "license", "color", "organization". Spanish pages use
  neutral Latin American Spanish with *usted*.
- **Numbers and prices:** `$30/Page` (certified, official), `10¢/Word` (professional),
  `$49/Page` (academic translation and evaluation). Ranges with en dash or hyphen, no spaces:
  "1-2 business days". Percentages with `%`, no space.
- **Phone:** `(800) 460-1536` always in this format.
- **Company name:** "The Spanish Group" in copy; "The Spanish Group LLC" in legal/footer/logo alt.
- **Headings:** Title Case; one H1 per page; H2 per section; no skipped levels in new content.
- **Punctuation:** curly apostrophes acceptable in copy (HOME mixes ' and ’; keep whatever the page
  uses consistently); em dash without spaces ("Don't worry—thorough…"); serial comma used
  ("Business, Academic, & Legal").
- **Asterisks** for promo conditions must have a matching footnote on the page.
- **Alt text:** describes the image or its function; logos as "<Org> logo"; never filenames,
  never duplicated generic text across different images.
- **SEO head pattern (HOME):** `<title>` = "<Primary keyword phrase> | The Spanish Group" (HOME is
  77 characters; target ≤ 60); meta description ≤ 160 characters, includes the main keyword and a
  benefit; canonical self-referencing absolute URL; OG and Twitter tags mirror title/description;
  `robots: index, follow`; JSON-LD `ProfessionalService` with phone +1-800-460-1536 and address
  1 Park Plaza, Suite 600, Irvine, CA 92614.

## 7. Brand-term dictionary — do NOT alter

Keep spelling, capitalization and meaning exactly as below. Do not "correct" these, translate them
on English pages, or swap them for synonyms.

| Term | Notes |
|---|---|
| The Spanish Group, The Spanish Group LLC, TSG | Company name. Never "Spanish Group" without "The" in prose. |
| certified translation(s) | Core service. Not "official translation" as a replacement. |
| sworn translation(s) | Distinct service, not a synonym for certified. |
| notarized translation(s) | Distinct service. |
| apostille / apostille translation / US Apostille services | Lowercase in running text, Title Case in headings. |
| USCIS | All caps. "USCIS Immigration Documents", "USCIS Immigration Translation". |
| ATA (American Translators Association) | All caps. "ATA Logo" asset. |
| ISO 9001:2015, ISO 17100:2015 | Exact format with colon and year. |
| Shopper Approved | Review platform name. |
| guaranteed acceptance / Guaranteed Acceptance for Certified Translations | Brand promise. |
| credential evaluation / foreign credential evaluation | Academic service. |
| Canadian immigration translations | Service name. |
| PCR/COVID-19 | Keep slash and caps. |
| API translation solutions | "API" all caps. |
| Get Free Quote, Get Instant Quote, Get Price, Order Translation, Track Order, Verify Price, Confirm Pricing | CTA labels. |
| Open 24/7 | Exact form. |
| (800) 460-1536 | Phone format. |
| Spanish: traducción certificada, traducción jurada, apostilla, USCIS, cotización | Spanish-page equivalents. |

## 8. Known issues on HOME (do not replicate; mention in "Comparison vs. HOME")

Found on 2026-10-22 capture:

1. **Language count inconsistency:** hero, H2 and feature boxes say 120 / 120+; meta description,
   OG/Twitter description and JSON-LD say "over 90 languages"; services grid says "89 other
   languages". Treat **120+** as current.
2. **Typos:** menu link "Turkish Translation **ervices**"; image alt "Place your order for
   **confimation**"; alt "**Loadig** GIF".
3. **Broken / suspicious hrefs:** French CTA `hhttps://thespanishgroup.org/facturation`; one
   "Get Instant Quote" menu link → `/screen-shot-2014-03-18-at-2-41-01-pm/`; "Translations for
   professional purposes" and "Language translation services" menu headers → `/translations/apostille-translation/`;
   header "Home" → `/translation/` instead of `/`; "Policies" with and without trailing slash.
4. **Alt text:** all ISO 17100 badge images reuse "Company Certified ISO 9001:2015"; hero avatars use
   Spanish alt "Foto de persona" on the English page; decorative images use "Curves" / "Background Image".
5. **Heading order:** H6 step titles directly under H2 in the process section; H4 used for card
   descriptions under H3.
6. **Fonts:** Roboto, Aller and Gotham are declared but not loaded → OS fallback fonts.
7. **Viewport:** `maximum-scale=1.0` blocks pinch zoom (WCAG 1.4.4 concern).
8. **Contrast:** white on `#47ACAD` = 2.70:1 (see section 4).
9. **Title length:** 77 characters (truncates in Google results).
10. **Commented-out promo** ("CYBER MONDAY SALE … 15% OFF") still in the HTML source.
11. "FAQ" subcopy: "99% of our client's questions" → should be "clients'".
12. Hero promo: "Up to 20% Off" heading, then "10% off" and "20% Off" lines with inconsistent capitalization.
