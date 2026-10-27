# Proofreading Report: Miami Translation Services (dev)

| | |
|---|---|
| Audited URL | https://devsite.thespanishgroup.net/translations/miami-translation-services-2/ |
| Date | 2026-10-22 |
| Capture | Firecrawl `rawHtml`, live fetch (`maxAge: 0`), HTTP 200, 324,090 bytes. Saved as `original.html`. |
| Screenshots | Firecrawl full-page, Chromium: `screenshots/mobile-375.png`, `tablet-768.png`, `desktop-1440.png` |
| References | `../_reference/style-guide.md` (HOME) and the approved location-page standard (Florida page, `TSG Landing Page/LANDING_PAGE_STANDARD.md`) |
| Page language | English (`lang="en"`) |
| Links checked | 9 internal destinations scraped (all main CTAs plus every suspicious path). The ~60 global nav links were not checked one by one. |

## Score

**Overall: 5.9 / 10** (before fixes). The copy and layout are mostly sound. The score is pulled down by the page's SEO setup and by trust claims that need confirming before publishing.

| Category | Score | Notes |
|---|---|---|
| Grammar and spelling | 7 | One subject–verb error, a few awkward or non-parallel phrases |
| Copy and tone vs. style guide | 5 | Two FAQ answers dodge the question; testimonials look written, not sourced |
| Design vs. template | 7 | Off-palette hover color; one CTA not pill-shaped |
| Buttons and CTAs | 7 | Labels and placement correct; 4 links go through redirects or a legacy page |
| Responsive (375 / 768 / 1440) | 6 | 375 and 1440 fine; hero breaks at exactly 768 px |
| Compatibility (Windows / Mac) | 6 | Modern CSS syntax that older Safari ignores |
| On-page SEO and accessibility | 3 | Broken title, empty meta, duplicate URL, wrong schema, alt text and contrast issues |

## Findings

Severity: **Critical** = blocks publishing. **High** = fix before publishing. **Medium** = should fix. **Low** = polish.
IDs in "Fix applied" match the "Changes applied to HTML" section below.

| # | Category | Severity | Location | Issue | Fix applied |
|---|---|---|---|---|---|
| 1 | SEO | Critical | URL / CMS | The slug ends in `-2` because `/translations/miami-translation-services/` already exists. That page is live on dev (HTTP 200), titled "» Miami Translation Services", and says "over 90 languages". Two Miami pages would compete for the same search queries. | None in HTML. In the CMS: retire the old page with a 301 to the new one, publish this page at `/translations/miami-translation-services/`, then update canonical, `og:url` and `twitter:url`. |
| 2 | SEO | Critical | `<head>` | `<title>` is "Certified Translations in Miami -": a dangling separator and no brand. Meta description, `og:title`, `og:description`, `twitter:title` and `twitter:description` are all empty. | C1, C2, C3 |
| 3 | Copy / trust | Critical | `section.testimonials-section` | The section says "Real reviews from clients across the city.", but Danielle P.'s quote contains, word for word, a sentence from the Florida page's Ashley T. (Tampa) testimonial: "The translations were accurate, professional, and easy to review." The three quotes also follow the Florida set's pattern (immigration / academic / business; Daniel P. → Danielle P.). This points to written copy, not sourced reviews. | None. Replace with sourced reviews, or remove the "Real reviews" line. The page already loads 9 real Shopper Approved reviews in a script (`reviews_section_ab216`), but none are from Miami. |
| 4 | SEO | High | JSON-LD `FAQPage` | Schema lists generic site-wide questions ("Tried, tested and trusted", "Validity of Certification"…) that are not on the page. | S1: rebuilt from the 6 visible FAQs, word for word |
| 5 | Copy / compliance | High | Hero eyebrow `.badge-approval` | "ATA CERTIFIED & USCIS APPROVED" contradicts the trust strip ("ATA Member"). ATA certification applies to individual translators, not companies, and USCIS does not approve translation providers: it requires a translator's certification of accuracy and competence (8 CFR 103.2(b)(3)). | None. This is approved template text; send it to the owner or legal for a wording decision (e.g. "ATA MEMBER & USCIS ACCEPTED"). |
| 6 | Compliance / design | High | `.why-choose-section` image | The photo shows the DHS seal and "U.S. Citizenship and Immigration Services" signage next to a "USCIS Accepted" badge, which suggests a government affiliation. The file is a reused blog asset (`Will-USCIS-Accept-a-Birth-Certificate-Translated-by-ChatGPT.png`) with alt "Translation signing". | None. Replace the image in the media library and give it a descriptive file name. |
| 7 | Grammar / claims | High | "Why it matters", paragraph 2 | "The Spanish Group translation agency in Miami **provide**…": subject–verb error. It also implies a physical Miami office, which contradicts FAQ 2 ("No [need to visit an office]"). | C11 |
| 8 | Responsive | High | `section.sectionHero` at 768 px | At exactly 768 px the whole hero (form, H1, intro, CTAs) sits in the left ~350 px and the right half is empty (`screenshots/tablet-768.png`). The mobile hero rules use `max-width: 768px`, while Bootstrap's `col-md-6` starts at 768 px, so both apply at once. | None. This is template CSS and needs a dev test. Suggested fix: end the mobile hero rules at 767.98px. |
| 9 | CTAs / links | High | Whole page | All 330 internal URLs, including canonical, `og:url` and form actions, point to `devsite.thespanishgroup.net`. This is expected on staging but must change on publish. | None (the preview relies on them). Check at publish. |
| 10 | CTAs / links | Medium | FAQ widget form, footer nav, main nav | 4 hrefs resolve only through redirects or point to a legacy page: FAQ form `action` → `/translations/translations/quotes/` (redirects); footer "Get Instant Quote" → `/translations/quotes-2/` (2014 legacy page titled "» Quotes", says "over 90 languages"); nav "Translation homepage" → `/translations/translations/` (redirects, ×2); nav Apostille → `/translations/translations/apostille-translation-services/` (redirects, ×2). | L1, L2, L3, L4 |
| 11 | Copy | Medium | FAQ 3 | "Are your certified translations suitable for immigration purposes?" The answer never says yes or no. | C13 |
| 12 | Copy | Medium | FAQ 4 | "How quickly can I receive a translation?" The answer gives no timeframe. | C14 (uses the turnaround already stated in the page's own USP bar) |
| 13 | Copy | Medium | `.global-partner-section` paragraph | Awkward sentence: "you shouldn't have to worry about having professional translation services being far away… with much greater convenience all around." The same defect is on the Florida page. | C12 |
| 14 | Accessibility | Medium | Hero `.reviewsImageRounded` | 4 avatar images use the Spanish alt text "Foto de persona" on an English page. | A1 (marked decorative, `alt=""`) |
| 15 | Accessibility | Medium | ISO badges (hero row + footer) | 22 ISO 17100 badge images have the alt text "Company Certified ISO 9001:2015". | A2 |
| 16 | Accessibility | Medium | `.how-it-works-section` | Subtitle and step text `#94A3B8` on `#1F3C5B` = 4.41:1, below AA 4.5:1 for small text. | A3 → `#CBD5E1` (7.62:1) |
| 17 | Accessibility | Medium | `.link-teal`, `.avatar-teal` | "Get Instant Quote" text link and "SM" avatar initials: `#0D9488` with white = 3.74:1. | A4, A5 → `#0F766E` (5.47:1) |
| 18 | Accessibility | Medium | Hero buttons, `.btn-terracotta`, FAQ widget button, "120+" stat | Brand teal `#47ACAD` with white = 2.70:1 (fails AA). | None, per style guide §4 (site-wide brand decision). Recommend `#2C8282` (4.54:1). |
| 19 | Compatibility | Medium | 14 `@media` rules in page CSS | Range syntax (`(width < 767px)`, `(width <= 768px)`…) is ignored by Safari/iOS before 16.4 and Chrome before 104. On those browsers the mobile hero rules (H1 36px, stacked layout) and the mobile review/CTA rules never apply. | X1: converted to equivalent `min-width` / `max-width` |
| 20 | Compatibility | Low | Page CSS (`.sectionHero .heading { & h1 … }` and others) | Native CSS nesting (`&`) needs Safari 16.5+ / Chrome 112+; older browsers drop those rules. Also present on HOME. | None (template CSS; flatten in the theme) |
| 21 | Design | Low | `.btn-terracotta:hover` | Hover turns burnt orange `#A84413`, which is not in the brand palette. | D1 → `#2C8282` |
| 22 | Design | Low | `.why-choose-section` "Get a Free Quote" | 8px corners (`rounded-3`); brand CTAs are pill-shaped. | D2 |
| 23 | Style guide | Low | Services cards H3 | "Varied Services" / "Convenience" differ from the approved card titles "Reliability" / "Simple Process". "Varied Services" also does not describe card 1, which is about Miami's multilingual population. | C5, C6 |
| 24 | SEO | Low | "Why it matters" H2 | "Why Professional Translation Matters in Miami" drops the "certified translation" keyword; the approved pattern is "Why Certified Translation Services Matter in {Location}". | C9 |
| 25 | Grammar | Low | "Why it matters", paragraph 1 | Non-parallel list: "legal, education, or employment-related". | C10 |
| 26 | Grammar | Low | Services card 2 | "make your order" (unidiomatic). | C7 |
| 27 | Copy | Low | Services card 3 | Repeats "all your … needs" in back-to-back sentences. | C8 |
| 28 | Grammar | Low | USP bar popup (top and bottom, ×2) | "For guaranteed same day delivery then please select…" | C15 |
| 29 | Copy | Low | USP bar popups | Popup text doesn't match its label: "100% Quality Guarantee" talks about 120 languages; "24/7 Customer Support" talks about delivery speed. | None (global copy; needs the owner's wording) |
| 30 | Responsive | Low | Header at 768 px | The fixed header overlaps the USP strip (labels clipped at the top), and the language selector appears twice. | None (template) |
| 31 | Responsive | Low | 375 px | The Why Choose photo is cropped mid-word ("U.S. Citizensh…"); the FAQ chevron shrinks on the two-line question 3; "Return to Top" is an unstyled browser button. | None (template) |

**Count: 3 Critical, 6 High, 10 Medium, 12 Low.**

## Comparison vs. HOME template

**Matches HOME:**
- Same global header, top bar (phone `(800) 460-1536`, Open 24/7), footer, and certification badges.
- Same Lato body / Roboto headings declaration.
- Same teal `#47ACAD` / navy `#1F3D5C`–`#2B4763` palette for brand elements.
- CTA labels and destinations follow the style guide: Order Translation → `/billing`, Get Free Quote / Get Instant Quote → `/translations/quotes/`.
- Brand terms (USCIS, ATA, ISO 9001:2015 / 17100:2015, certified translation) are used correctly.

**Deviates by design:** this page uses the location-landing template, not the HOME layout. Its section order (hero, price ticker, trust strip, services cards, why it matters, how it works, why choose, access anywhere, testimonials, FAQ) matches the approved Florida standard, so section structure was judged against that standard. Deviations from the standard are findings 23 and 24, plus:
- FAQ questions are worded differently ("What documents…" vs. "What types of documents…"). Accepted.
- The services H2 says "in Miami" instead of "Throughout {Location}", which suits a city page.
- The services subtitle is "Supporting Miami's International Community" instead of "Accurate Translations for Individuals, Businesses, and Organizations". Accepted as an equally specific angle.

**Colors outside the HOME palette:** the landing template brings in Tailwind-style colors:
- peach icon box `#FDEEE9` and decorative border `#EBD2C5`
- orange avatar `#C2531A`
- teal `#0D9488`
- slate text `#94A3B8` and `#334155`
- classes named `terracotta` that actually render brand teal

The off-palette hover was fixed (D1), and the two contrast failures were fixed (A3–A5). The other accent colors are kept because they're part of the approved Florida template.

**Same defects as HOME:** ISO 17100 alt text (fixed here); Spanish avatar alt text (fixed here); brand-teal contrast; Roboto declared but never loaded (headings fall back to Arial on Windows and Helvetica on Mac).

**Better than HOME:**
- The visible copy says 120+ languages throughout, with no "90" contradictions.
- The viewport has no `maximum-scale=1.0`, so pinch-zoom works.
- Every price claim matches HOME (10¢ per word).

## Changes applied to HTML

Every difference between `original.html` and `proofread.html` is listed here, and nothing else changed. This was checked with a line diff: 62 changed hunks, plus one class change (D2).

### `<head>`: SEO
- **C1** `<title>`: `Certified Translations in Miami -` → `Miami Translation Services | The Spanish Group` (46 characters)
- **C2** `meta name="description"`: `""` → `Get Miami translation services with same-day delivery, notarized copies and 120+ languages. Only 10¢ per word.` (110 characters)
- **C3** `og:title` and `twitter:title`: `""` → `Miami Translation Services | The Spanish Group`. `og:description` and `twitter:description`: `""` → the same text as C2.
- **S1** JSON-LD `FAQPage`: the generic site-wide Q&A list → the 6 visible questions and answers, word for word, including the C13 and C14 wording.

### Page CSS (inline `<style>` blocks)
- **X1** Media queries, 14 occurrences (one is inside the script-injected reviews block at line 4634):
  - `(width < 767px)` and `(width<767px)` → `(max-width: 766.98px)` ×6
  - `(width > 767px)` → `(min-width: 767.02px)` ×1
  - `(width < 768px)` → `(max-width: 767.98px)` ×2
  - `(width <= 768px)` → `(max-width: 768px)` ×3
  - `(width > 768px)` → `(min-width: 768.02px)` ×2

  Behavior is unchanged in modern browsers.
- **A3** `.text-secondary-custom { color: rgb(148, 163, 184) }` → `rgb(203, 213, 225)`
- **A4** `.link-teal { color: rgb(13, 148, 136) }` → `rgb(15, 118, 110)`
- **A5** `.avatar-teal { background-color: rgb(13, 148, 136) }` → `rgb(15, 118, 110)`
- **D1** `.btn-terracotta:hover` background and border `rgb(168, 68, 19)` → `rgb(44, 130, 130)`

### Header / navigation (global)
- **L3** "Translation homepage" link (×2): `…/translations/translations/` → `…/translations/`
- **L4** Apostille link (×2): `…/translations/translations/apostille-translation-services/` → `…/translations/apostille-translation-services/`
- **C15** USP popup (×2, top and bottom bars): `For guaranteed same day delivery then please select Urgent Translation Service…` → `For guaranteed same-day delivery, please select Urgent Translation Service…`

### Hero
- **A1** 4 avatar images: `alt="Foto de persona"` → `alt=""`
- **A2** (hero badge row, 9 images) ISO 17100 badges: `alt="Company Certified ISO 9001:2015"` → `alt="Company Certified ISO 17100:2015"`

### Services cards
- **C5** Card 1 H3: `Varied Services` → `Reliability`
- **C6** Card 2 H3: `Convenience` → `Simple Process`
- **C7** Card 2: `upload your document and make your order` → `upload your document and place your order`
- **C8** Card 3: `our language experts can help you with all your translation needs in Miami.` → `our language experts can help you with any translation project in Miami.`

### Why it matters
- **C9** H2: `Why Professional Translation Matters in Miami` → `Why Certified Translation Services Matter in Miami`
- **C10** P1: `meet legal, education, or employment-related requirements` → `meet legal, educational, or employment-related requirements`
- **C11** P2: `The Spanish Group translation agency in Miami provide professional language translation services for all personal and commercial translation needs.` → `The Spanish Group provides professional language translation services in Miami for all personal and commercial translation needs.`

### Why Choose The Spanish Group
- **D2** "Get a Free Quote" button class: `rounded-3` → `rounded-pill`

### Access anywhere
- **C12** Paragraph:
  - Before: `Wherever you are in Miami, you shouldn't have to worry about having professional translation services being far away. Whether you need a single personal document translated or assistance with a larger-scale project, our team will find the most suitable solutions for you, which will help you get professional translation results with much greater convenience all around.`
  - After: `Wherever you are in Miami, you shouldn’t have to travel to find professional translation services. Whether you need a single personal document translated or assistance with a larger-scale project, our team will find the most suitable solution for you and deliver professional results with greater convenience.`

### FAQ
- **C13** FAQ 3 answer:
  - Before: `We offer certified translation services in Miami for a broad range of … documents in more than 120 languages. However, it is advisable…`
  - After: `Yes. Our certified translations are accepted by USCIS, and we translate a broad range of personal, legal, academic, medical, immigration, and business-related documents in more than 120 languages. However, it is advisable to contact the relevant institution to confirm whether our services meet their specific requirements.`
- **C14** FAQ 4 answer:
  - Before: `The delivery time for document translation depends on the complexity and length of the document, as well as the type of service requested. Nevertheless, we offer quick and affordable translation services to ensure you receive your documents in time.`
  - After: `Most documents are delivered within 1-2 business days with our standard First Class speed. For guaranteed same-day delivery, select Urgent Translation Service when placing your order. Delivery time can vary with the length and complexity of the document.`
- **L1** Quote widget form: `action="…/translations/translations/quotes/"` → `action="…/translations/quotes/"`

### Footer
- **A2** (footer, 13 images) ISO 17100 badges: alt `…ISO 9001:2015` → `…ISO 17100:2015`
- **L2** Site Navigation "Get Instant Quote": `…/translations/quotes-2/` → `…/translations/quotes/`

## Not verifiable via scraping

- **Safari on macOS/iOS and Edge/Chrome on Windows:** screenshots were taken in Chromium only. Font fallback (Roboto → Arial/Helvetica), the X1 media-query change, and CSS nesting support all need a manual check on a real iPhone (ideally iOS 15–16.3 too), Mac Safari, and Windows Edge.
- **"Miami Courts" in the trust strip:** a claim of court acceptance that only the business can confirm. There is also no single "Miami Courts" body (the local courts are Miami-Dade County Court and the 11th Judicial Circuit).
- **Testimonial sources:** whether Sofia M., Carlos R. and Danielle P. are real customers who consented. Finding 3 is based only on the text overlap with the Florida page.
- **Discount disclaimer on desktop:** the hero shows "Up to 20% Off" (A/B variant), and the matching footer disclaimer appears at 375 px. At 1440 px it was not visible in the screenshot, possibly hidden behind the sticky "Order Translation" bar. Check by hand in each A/B variant.
- **Forms:** the lead form ("Get Started") and quote widget were not submitted, per the project rules.
- **JavaScript behavior:** FAQ accordion, price marquee, language switcher, and A/B variant switching were seen only in static screenshots.
- **Global nav and footer links:** about 60 links were not checked one by one. The 9 checked were `/billing`, `/translations/quotes/`, `/translations/quotes-2/`, `/translations/translations/quotes/`, `/translations/translations/`, `/translations/translations/apostille-translation-services/`, `/translations/?order-status=tracker` (shows "Order Not Found" without an order ID, as expected), `/my-account/order-history/`, and `/translations/miami-translation-services/`.
- **Performance:** image weights and Core Web Vitals were not measured.
- **Editorial choice:** the "Spanish" language card shows the Mexican flag. This was left as is.
