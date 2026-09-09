import re
import os

def check():
    path = 'guide/annapurna-base-camp-trek-september.html'
    content = open(path, encoding='utf-8').read()
    
    m = re.search(r'<article[\s\S]*?</article>', content)
    art = m.group(0) if m else content
    
    links = re.findall(r'<a\s+[^>]*?href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>', art, re.DOTALL)
    print(f"Total links inside article: {len(links)}")
    
    non_hash = []
    has_html_extension = []
    
    for href, text in links:
        clean_text = re.sub(r'<[^<]+?>', '', text).strip()
        if href.startswith('#'):
            continue
        non_hash.append((href, clean_text))
        if '.html' in href:
            has_html_extension.append((href, clean_text))
            
    print(f"\nNon-anchor internal/external links ({len(non_hash)}):")
    for h, t in non_hash:
        print(f"  {h:60} --> {t[:35]}")
        
    print(f"\nLinks with .html extension: {len(has_html_extension)}")
    if has_html_extension:
        for h, t in has_html_extension:
            print(f"  FAIL: {h}")
    else:
        print("  PASS: Zero .html extensions found! All URLs are clean & SEO optimized.")

if __name__ == '__main__':
    check()
