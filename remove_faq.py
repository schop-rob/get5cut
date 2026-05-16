import os
import re

def remove_faq_schema(directory):
    count = 0
    faq_pattern = re.compile(r'<script type="application/ld\+json">\s*\{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"FAQPage"[\s\S]*?</script>', re.MULTILINE)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if faq_pattern.search(content):
                    new_content = faq_pattern.sub('', content)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Removed FAQPage schema from {filepath}")
                    count += 1
    print(f"Total files updated: {count}")

remove_faq_schema('.')
