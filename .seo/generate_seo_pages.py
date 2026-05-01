import json
import os
import re

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, 'index.html')
DATA_PATH = os.path.join(BASE_DIR, '.seo', 'seo_data.json')

def load_template():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def inject_faqs(html, faqs):
    # Build HTML FAQs
    faq_html = '<h3>Frequently asked questions</h3>\n'
    for faq in faqs:
        faq_html += f'''            <details>
                <summary>{faq["q"]}</summary>
                <p>{faq["a"]}</p>
            </details>
'''
    # Replace the FAQ section
    html = re.sub(r'<h3>Frequently asked questions</h3>.*?</div>', faq_html + '        </div>', html, flags=re.DOTALL)
    
    # Update FAQ schema
    schema_entities = []
    for faq in faqs:
        schema_entities.append(f'''            {{
                "@type": "Question",
                "name": "{faq["q"]}",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "{faq["a"]}"
                }}
            }}''')
    
    schema_json = ',\n'.join(schema_entities)
    
    # Replace FAQ schema content
    html = re.sub(r'"mainEntity": \[.*?\]', f'"mainEntity": [\n{schema_json}\n        ]', html, flags=re.DOTALL)
    return html

def build_page(slug, data, base_path, category_folder):
    html = load_template()
    
    # 1. Meta tags
    html = re.sub(r'<title>.*?</title>', f'<title>{data["meta_title"]}</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{data["meta_description"]}">', html)
    html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{data["meta_title"]}">', html)
    html = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{data["meta_description"]}">', html)
    html = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{data["meta_title"]}">', html)
    html = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{data["meta_description"]}">', html)
    
    # 2. Canonical URL
    html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://get5cut.com/{category_folder}/{slug}/">', html)
    
    # 3. Headers & Copy
    # Replace the brand h1 and tagline
    new_header = f'''<h1 class="brand" style="font-size: 36px; line-height: 1.2; letter-spacing: -0.02em; text-transform: none; margin-bottom: 16px;"><span class="highlight">{data["h1"]}</span></h1>
        <h2 class="tagline">{data["tagline"]}</h2>
        
        <div style="text-align: left; margin-bottom: 48px;">
            <p style="font-size: 16px; color: #444; line-height: 1.6;">{data["paragraph_1"]}</p>
        </div>'''
    
    html = re.sub(r'<h1 class="brand">.*?<h2 class="tagline">.*?</h2>', new_header, html, flags=re.DOTALL)
    
    # Remove the callout block specific to the homepage
    html = re.sub(r'<div class="callout">.*?</div>\s*<div class="stat-label">.*?</div>\s*</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div class="callout">.*?</div>', '', html, flags=re.DOTALL)
    
    # 4. Inject FAQs and Schema
    if "faqs" in data:
        html = inject_faqs(html, data["faqs"])
        
    # Write to disk
    output_dir = os.path.join(BASE_DIR, category_folder, slug)
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Generated: {category_folder}/{slug}/index.html")
    return f"https://get5cut.com/{category_folder}/{slug}/"

def update_sitemap(new_urls):
    sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
    if not os.path.exists(sitemap_path):
        return
        
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Insert before </urlset>
    new_xml = ""
    for url in new_urls:
        if url not in content:
            new_xml += f'''
    <url>
        <loc>{url}</loc>
        <changefreq>weekly</changefreq>
        <priority>0.7</priority>
    </url>'''
            
    if new_xml:
        content = content.replace('</urlset>', f'{new_xml}\n</urlset>')
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added {len(new_urls)} new URLs to sitemap.xml")

def main():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    all_urls = []
    
    # Process Use Cases
    for item in data.get('use-cases', []):
        url = build_page(item['slug'], item, BASE_DIR, 'use-cases')
        all_urls.append(url)
        
    # Process Alternatives
    for item in data.get('alternatives', []):
        url = build_page(item['slug'], item, BASE_DIR, 'alternatives')
        all_urls.append(url)
        
    update_sitemap(all_urls)

if __name__ == '__main__':
    main()
