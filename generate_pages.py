import os
import json

from i18n import LANGS, faq_details, hreflang_links, lang_switch, module

languages = {code: module(code).HOME for code, *_ in LANGS}

html_template = """<!DOCTYPE html>
<html lang="{lang_code}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="icon" type="image/svg+xml" href="/icon.svg">
    <link rel="icon" type="image/png" href="/favicon.png">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="canonical" href="https://get5cut.com{canonical_path}">
{hreflang_links}
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{og_description}">
    <meta property="og:url" content="https://get5cut.com{canonical_path}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://get5cut.com/assets/og-card.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{og_title}">
    <meta name="twitter:description" content="{og_description}">
    <meta name="twitter:image" content="https://get5cut.com/assets/og-card.png">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "5cut",
        "operatingSystem": "iOS",
        "applicationCategory": "MultimediaApplication",
        "description": "{description}",
        "featureList": "In-app recorder, AI summaries, Export to Apple Notes/Anki/Notion/Obsidian, Silence removal, on-device transcription in 30+ languages, speaker identification",
        "screenshot": "https://get5cut.com/assets/iphone-transcript.png",
        "author": {{
            "@type": "Person",
            "name": "Robin Schöppner",
            "url": "https://get5cut.com/"
        }},
        "softwareVersion": "1.2.5",
        "url": "https://get5cut.com{canonical_path}",
        "sameAs": "https://apps.apple.com/app/5cut/id6758529319",
        "offers": {{
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
        }}
    }}
    </script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif;
            background: #F5F5F5;
            color: #111;
            min-height: 100vh;
            padding: 40px 24px;
        }}
        .container {{
            max-width: 1040px;
            width: 100%;
            margin: 0 auto;
        }}
        .hero {{
            min-height: calc(100vh - 96px);
            display: grid;
            grid-template-columns: minmax(0, 0.9fr) minmax(360px, 1.1fr);
            gap: 56px;
            align-items: center;
        }}
        .hero-copy {{
            text-align: left;
        }}
        .brand {{
            font-family: Impact, 'Arial Black', sans-serif;
            font-size: 72px;
            font-weight: 900;
            letter-spacing: 0;
            text-transform: uppercase;
            line-height: 1;
            margin-bottom: 8px;
        }}
        .highlight {{
            position: relative;
            display: inline;
        }}
        .highlight::after {{
            content: '';
            position: absolute;
            bottom: 0.05em;
            left: -0.05em;
            right: -0.05em;
            height: 0.3em;
            background: #FFCC00;
            z-index: -1;
        }}
        .tagline {{
            font-size: 30px;
            line-height: 1.08;
            font-weight: 400;
            color: #555;
            margin-bottom: 28px;
            letter-spacing: 0;
        }}
        .hero-facts {{
            font-size: 18px;
            line-height: 1.5;
            color: #333;
            margin: -12px 0 24px;
            max-width: 34em;
        }}
        .hero-proof {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 24px;
        }}
        .proof-pill {{
            border: 1px solid #D7D1C6;
            border-radius: 999px;
            padding: 8px 12px;
            font-size: 13px;
            color: #333;
            background: #fff;
        }}
        .cta-container {{
            margin: 24px 0 32px 0;
            text-align: left;
        }}
        @media (max-width: 820px) {{
            .cta-container {{
                text-align: center;
            }}
        }}
        .cta-subtext {{
            font-size: 13px;
            color: #666;
            margin-bottom: 6px;
            font-weight: 500;
        }}
        .hero-visual {{
            position: relative;
            min-height: 570px;
        }}
        .phone-shot {{
            position: absolute;
            width: min(31vw, 250px);
            max-width: 250px;
            filter: drop-shadow(0 24px 48px rgba(17, 17, 17, 0.18));
        }}
        .phone-shot.recorder {{
            left: 0;
            top: 16px;
            transform: rotate(-4deg);
        }}
        .phone-shot.editor {{
            left: 30%;
            top: 58px;
            z-index: 2;
            filter: drop-shadow(0 20px 40px rgba(17, 17, 17, 0.3));
        }}
        .phone-shot.transcript {{
            right: 0;
            top: 16px;
            transform: rotate(4deg);
        }}
        .hero-note {{
            position: absolute;
            left: 12%;
            right: 12%;
            bottom: 12px;
            z-index: 10;
            background: #111;
            color: #fff;
            padding: 16px 18px;
            border-radius: 8px;
            font-size: 15px;
            line-height: 1.35;
            text-align: center;
        }}
        .features {{
            text-align: left;
            margin-bottom: 48px;
        }}
        .feature {{
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 20px;
        }}
        .feature-icon {{
            width: 32px;
            height: 32px;
            background: #111;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            font-size: 16px;
        }}
        .feature-text h3 {{
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 2px;
        }}
        .feature-text p {{
            font-size: 13px;
            color: #666;
            line-height: 1.4;
        }}
        .app-icon {{
            width: 128px;
            height: 128px;
            border-radius: 22.37%;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            margin-bottom: 24px;
        }}
        .use-cases {{
            text-align: left;
            margin-bottom: 48px;
        }}
        .use-cases h2 {{
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 8px;
        }}
        .use-cases p {{
            font-size: 13px;
            color: #666;
            line-height: 1.5;
            margin-bottom: 8px;
        }}
        .privacy-box {{
            background: #E8F5E9;
            border: 1px solid #4CAF50;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 48px;
            text-align: left;
        }}
        .privacy-box h2 {{
            font-size: 16px;
            font-weight: 700;
            color: #2E7D32;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .privacy-box p {{
            font-size: 13px;
            color: #388E3C;
            line-height: 1.5;
        }}
        .app-store-badge {{
            display: inline-block;
            margin-bottom: 32px;
        }}
        .app-store-badge img {{
            height: 54px;
        }}
        .divider {{
            width: 120px;
            height: 6px;
            background: #FFCC00;
            margin: 0 auto 32px;
        }}
        .lang-switch {{
            position: absolute;
            top: 16px;
            right: 24px;
            font-size: 13px;
            background: #fff;
            padding: 4px 12px;
            border-radius: 16px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}
        .lang-switch a {{
            color: #666;
            text-decoration: none;
            margin: 0 4px;
        }}
        .lang-switch a.active {{
            font-weight: 700;
            color: #111;
        }}
        .lang-switch a:hover {{
            text-decoration: underline;
        }}
        @media (max-width: 600px) {{
            .lang-switch {{
                position: static;
                display: block;
                margin: 12px 16px 0;
                text-align: center;
                line-height: 1.8;
            }}
        }}
        footer {{
            margin: 64px auto 0;
            font-size: 13px;
            color: #777;
            text-align: left;
            width: 100%;
            max-width: 800px;
        }}
        .footer-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 32px;
            margin-bottom: 48px;
        }}
        .footer-col h4 {{
            font-size: 14px;
            color: #111;
            margin-bottom: 16px;
        }}
        .footer-col a {{
            display: block;
            color: #666;
            text-decoration: none;
            margin-bottom: 8px;
        }}
        .footer-col a:hover {{
            text-decoration: underline;
            color: #111;
        }}
        .copyright {{
            text-align: center;
            font-size: 12px;
            color: #999;
            border-top: 1px solid #eee;
            padding-top: 24px;
        }}
        .faq {{
            text-align: left;
            margin-bottom: 48px;
        }}
        .faq h2 {{
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 12px;
        }}
        .faq details {{
            margin-bottom: 8px;
            border-bottom: 1px solid #E0E0E0;
        }}
        .faq summary {{
            font-size: 14px;
            font-weight: 600;
            padding: 10px 0;
            cursor: pointer;
            list-style: none;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .faq summary::-webkit-details-marker {{ display: none; }}
        .faq summary::after {{
            content: '+';
            font-size: 18px;
            color: #999;
            transition: transform 0.2s;
        }}
        .faq details[open] summary::after {{
            content: '−';
        }}
        .faq details p {{
            font-size: 13px;
            color: #666;
            line-height: 1.5;
            padding: 0 0 12px;
        }}
        .how-it-works {{
            text-align: left;
            margin-bottom: 48px;
        }}
        .how-it-works h2 {{
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 12px;
        }}
        .step {{
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 16px;
        }}
        .step-number {{
            width: 24px;
            height: 24px;
            background: #FFCC00;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            font-weight: 700;
            flex-shrink: 0;
        }}
        .step p {{
            font-size: 13px;
            color: #666;
            line-height: 1.4;
        }}
        .step strong {{
            color: #111;
        }}
        .callout {{
            background: #111;
            color: #fff;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 48px;
            text-align: center;
        }}
        .callout .stat {{
            font-family: Impact, 'Arial Black', sans-serif;
            font-size: 48px;
            letter-spacing: -0.03em;
            line-height: 1;
            margin-bottom: 4px;
        }}
        .callout .stat-label {{
            font-size: 14px;
            color: #999;
        }}
        @media (max-width: 820px) {{
            body {{ padding: 32px 18px; }}
            .hero {{
                min-height: auto;
                grid-template-columns: 1fr;
                gap: 28px;
            }}
            .hero-copy {{ text-align: center; }}
            .brand {{ font-size: 56px; }}
            .tagline {{ font-size: 25px; }}
            .hero-proof {{ justify-content: center; }}
            .hero-visual {{
                min-height: 500px;
                overflow: hidden;
            }}
            .phone-shot {{ width: 210px; }}
            .phone-shot.recorder {{ left: -6px; }}
            .phone-shot.editor {{ left: calc(50% - 105px); top: 46px; }}
            .phone-shot.transcript {{ right: -6px; }}
            .hero-note {{ left: 0; right: 0; bottom: 0; }}
        }}
    </style>
    <script defer data-domain="get5cut.com" src="https://plausible.io/js/script.js"></script>
</head>
<body>
    <div class="lang-switch">
{lang_switch}
    </div>
    <main class="container">
        <section class="hero">
            <div class="hero-copy">
                <img src="/icon.svg" alt="{alt_icon}" class="app-icon">
                <h1 class="brand"><span class="highlight">{brand}</span>{brand_suffix}</h1>
                <h2 class="tagline">{tagline}</h2>
                <p class="hero-facts">{subhead_features}</p>
                <div class="hero-proof">
                    <span class="proof-pill">{proof1}</span>
                    <span class="proof-pill">{proof2}</span>
                    <span class="proof-pill">{proof3}</span>
                </div>
                <div class="cta-container">
                    <p class="cta-subtext">{cta_subtext}</p>
                    <a class="app-store-badge" href="https://apps.apple.com/app/5cut/id6758529319?pt=128495158&ct=web_home&mt=8">
                        <img src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" alt="{alt_badge}">
                    </a>
                </div>
            </div>
            <div class="hero-visual" aria-label="{aria_screens}">
                <img src="/assets/iphone-recorder.png" alt="{alt_recorder}" class="phone-shot recorder">
                <img src="/assets/iphone-transcript.png" alt="{alt_transcript}" class="phone-shot editor">
                <img src="/assets/iphone-editor.png" alt="{alt_editor}" class="phone-shot transcript">
                <p class="hero-note">{hero_note_desc}</p>
            </div>
        </section>

        <div class="divider"></div>

        <article class="features">
            <div class="feature">
                <div class="feature-icon"><svg width="16" height="16" fill="none" stroke="white" stroke-width="2"><circle cx="8" cy="8" r="4"/><path d="M14 8a6 6 0 11-12 0 6 6 0 0112 0z"/></svg></div>
                <div class="feature-text">
                    <h3>{feat1_title}</h3>
                    <p>{feat1_desc}</p>
                </div>
            </div>
            <div class="feature">
                <div class="feature-icon"><svg width="16" height="16" fill="none" stroke="white" stroke-width="2"><path d="M4 2v12M12 2v12M1 8h14"/></svg></div>
                <div class="feature-text">
                    <h3>{feat2_title}</h3>
                    <p>{feat2_desc}</p>
                </div>
            </div>
            <div class="feature">
                <div class="feature-icon"><svg width="16" height="16" fill="none" stroke="white" stroke-width="2"><path d="M2 3h12v10H2z"/><path d="M5 7h6M5 9h4"/></svg></div>
                <div class="feature-text">
                    <h3>{feat3_title}</h3>
                    <p>{feat3_desc}</p>
                </div>
            </div>
            <div class="feature">
                <div class="feature-icon"><svg width="16" height="16" fill="none" stroke="white" stroke-width="2"><path d="M2 4h12M2 8h8M2 12h10"/></svg></div>
                <div class="feature-text">
                    <h3>{feat4_title}</h3>
                    <p>{feat4_desc}</p>
                </div>
            </div>
            <div class="feature">
                <div class="feature-icon"><svg width="16" height="16" fill="none" stroke="white" stroke-width="2"><circle cx="5" cy="6" r="3"/><circle cx="11" cy="6" r="3"/><path d="M2 14c0-2 2-3 3-3s3 1 3 3M8 14c0-2 2-3 3-3s3 1 3 3"/></svg></div>
                <div class="feature-text">
                    <h3>{feat5_title}</h3>
                    <p>{feat5_desc}</p>
                </div>
            </div>
        </article>

        <section class="how-it-works">
            <h2>{how_it_works}</h2>
            <div class="step">
                <div class="step-number">1</div>
                <p>{step1}</p>
            </div>
            <div class="step">
                <div class="step-number">2</div>
                <p>{step2}</p>
            </div>
            <div class="step">
                <div class="step-number">3</div>
                <p>{step3}</p>
            </div>
            <div class="step">
                <div class="step-number">4</div>
                <p>{step4}</p>
            </div>
        </section>

        <section class="use-cases">
            <h2>{perfect_for}</h2>
            <p>{perfect_for_desc1}</p>
            <p>{perfect_for_desc2}</p>
        </section>




        <section class="privacy-box">
            <h2><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>{privacy_title}</h2>
            <p>{privacy_desc}</p>
        </section>

        <div class="cta-container" style="text-align: center;">
            <p class="cta-subtext">{cta_subtext}</p>
            <a class="app-store-badge" href="https://apps.apple.com/app/5cut/id6758529319?pt=128495158&ct=web_footer&mt=8">
                <img src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" alt="{alt_badge}">
            </a>
        </div>

        <section class="faq">
            <h2>{faq}</h2>
{faq_items_html}
        </section>
    </main>

    <footer>
        <div class="footer-grid">
            <div class="footer-col">
                <h4>{footer_use_cases}</h4>
                <a href="{prefix}/use-cases/remove-silence-from-zoom/">{footer_zoom}</a>
                <a href="{prefix}/use-cases/remove-silence-from-obs/">{footer_obs}</a>
                <a href="{prefix}/remove-silence-from-lectures/">{footer_lectures}</a>
                <a href="{prefix}/cut-background-noise-from-recordings/">{footer_noise}</a>
                <a href="{prefix}/podcast-silence-remover/">{footer_podcasts}</a>
                <a href="{prefix}/free-jumpcut-app/">{footer_jumpcut}</a>
                <a href="{prefix}/smartphone-video-editor/">{footer_editor}</a>
            </div>
            <div class="footer-col">
                <h4>{footer_alternatives}</h4>
                <a href="{prefix}/alternatives/timebolt-alternative/">{footer_timebolt}</a>
                <a href="/alternatives/otter-alternative/">{footer_otter}</a>
            </div>
            <div class="footer-col">
                <h4>{footer_study_fields}</h4>
                <a href="{prefix}/best-app-for-medical-school-lectures/">{footer_medical}</a>
                <a href="{prefix}/best-app-for-law-school-recordings/">{footer_law}</a>
            </div>
            <div class="footer-col">
                <h4>{footer_legal}</h4>
                <a href="/support/">{footer_support}</a>
                <a href="/privacy/">{footer_privacy}</a>
                <a href="/terms/">{footer_terms}</a>
                <a href="/impressum/">Impressum</a>
            </div>
        </div>
        <p class="copyright">&copy; 2026 Robin Sch&ouml;ppner</p>
    </footer>
</body>
</html>
"""

for lang, directory, _, _ in LANGS:
    data = languages[lang]
    if directory != "." and not os.path.exists(directory):
        os.makedirs(directory)
    
    canonical_path = "/" if directory == "." else f"/{directory}/"
    
    prefix = "" if directory == "." else f"/{directory}"
    
    # Merge context
    context = {
        **data,
        "canonical_path": canonical_path,
        "prefix": prefix,
        "hreflang_links": hreflang_links(),
        "lang_switch": lang_switch(lang),
        "faq_items_html": faq_details(data["faq_items"]),
    }
    
    output_html = html_template.format(**context)
    
    filepath = os.path.join(directory, "index.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(output_html)
        
    print(f"Generated {filepath}")
