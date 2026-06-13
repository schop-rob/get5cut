# SEO Audit Report: get5cut

- **URL**: `https://get5cut.com`
- **Audit Date**: `2026-06-13`
- **Status**: **Fully Optimized**
- **Overall Score**: `95/100` (Excellent)

---

## 📊 Score Card

| Category | Weight | Score | Status |
| :--- | :---: | :---: | :---: |
| **Technical SEO & Indexing** | 25% | 98/100 | ✅ Pass |
| **Structured Data (Schema)** | 15% | 100/100 | ✅ Pass |
| **Sitemap & Canonicalization** | 15% | 100/100 | ✅ Pass |
| **Hreflang & Internationalization** | 15% | 100/100 | ✅ Pass |
| **Headings & Hierarchy** | 10% | 100/100 | ✅ Pass |
| **AI Search Readiness (GEO/AEO)** | 10% | 95/100 | ✅ Pass |
| **llms.txt & Crawler Management** | 10% | 100/100 | ✅ Pass |

---

## 🔍 Detailed Findings & Audited Areas

### 1. Structured Data (Schema)
- **Status**: ✅ **Pass (Fully Compliant)**
- **Audit Findings**:
  - **Homepage (`index.html`)**: Contains a valid `SoftwareApplication` JSON-LD schema with author (`Robin Schöppner`), operating system (`iOS`), and version info.
  - **Inner Pages**: Generated pages contain a clean `Article` JSON-LD schema with author, publisher (`Organization`), and self-referencing `mainEntityOfPage` configuration.
  - **Guidelines Alignment**: 
    - The deprecated and restricted `FAQPage` rich results schema has been **fully removed** from the homepage (`generate_pages.py` and all localized `index.html` files).
    - No faked user reviews, faked ratings, or deprecated `HowTo` schemas exist on any page.

### 2. Sitemap & Canonicalization
- **Status**: ✅ **Pass (Correctly Configured)**
- **Audit Findings**:
  - **Sitemap (`sitemap.xml`)**: Up to date and lists all canonical page versions for all supported languages (EN, DE, ZH, FR, VI, ES).
  - **Canonical URL Matching**: Every generated page has a self-referencing `<link rel="canonical">` tag pointing to its correct absolute HTTPS URL. Trailing slashes are consistently applied across both the sitemap and HTML files (e.g., `https://get5cut.com/use-cases/remove-silence-from-zoom/`).

### 3. Hreflang Tags (International SEO)
- **Status**: ✅ **Pass (Validated)**
- **Audit Findings**:
  - All homepage variations correctly cross-reference each other using standard hreflang alternates (e.g., `hreflang="zh-Hans"` pointing to the `/zh/` directory).
  - Inner pages use `generate_inner_pages.py` to correctly generate cross-referencing hreflangs for the specific page paths (e.g., `<link rel="alternate" hreflang="de" href="https://get5cut.com/de/speed-up-zoom-recordings/">`), avoiding the common error of pointing inner page hreflangs to the homepages.
  - `x-default` is correctly mapped to the root English URL.

### 4. Headings & Hierarchy
- **Status**: ✅ **Pass (Logical Sequence)**
- **Audit Findings**:
  - The hierarchy is completely sequential across the site.
  - **Homepage**: Starts with a single `<h1>` for the brand name + tagline-suffix, followed by `<h2>` for taglines/sections, and `<h3>` for feature details.
  - **Inner Pages**: A single `<h1>` is dynamically populated for the page title (`page_h1`), followed by an `<h2>` tagline/intro subheadings, and `<h3>` details. There are no skipped levels.

### 5. AI Search Readiness (GEO/AEO) & Semantic Content
- **Status**: ✅ **Pass (Highly Optimized)**
- **Audit Findings**:
  - **Structured Elements**: Use cases and features leverage detailed tables (such as the transcription engine comparison table in `offline-lecture-transcription-iphone/`), bullet points, and ordered lists. Generative AI models and Answer Engines heavily prioritize structured table/list data for summarizing and referencing.
  - **Clear Headers**: Subheadings directly pose and answer search intent queries, making the site highly eligible for Featured Snippets, People Also Ask (PAA), and AI overview citations.

### 6. Crawler Management & `llms.txt`
- **Status**: ✅ **Pass (Up to date)**
- **Audit Findings**:
  - **`robots.txt`**: Standard user-agent policy allows all crawlers (including AI crawlers like `GPTBot`, `ClaudeBot`, and `PerplexityBot`), which is required for GEO/AEO optimization so AI search engines can ingest the site and attribute citations.
  - **`llms.txt`**: A curated machine-readable description of 5cut, listing all key landing pages, features, and privacy parameters. **Successfully updated** to list all 14 primary use-case and alternative landing pages.

---

## 📈 Recommendation Summary

| Severity | Element | Finding / Improvement | Fix Status |
| :--- | :--- | :--- | :--- |
| ✅ **Pass** | Schema | Removed restricted `FAQPage` schema from all pages | **Fixed** |
| ✅ **Pass** | `llms.txt` | Expanded key pages list to include all 14 use-case and alternative URLs | **Fixed** |
| ✅ **Pass** | Canonical | Corrected localized canonical links and trailing slash consistency | **Verified** |
| ✅ **Pass** | Hreflang | Ensured localized inner pages point to correct path-level alternate links | **Verified** |
| ✅ **Pass** | Headings | Logical sequential hierarchy without skipped heading levels | **Verified** |
