import re

with open('guide/annapurna-base-camp-trek-september.html', 'r', encoding='utf-8') as f:
    content = f.read()

article_match = re.search(r'<article[\s\S]*?</article>', content)
if article_match:
    art = article_match.group(0)
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', art)
    print(f"Total links inside <article>: {len(links)}")
    for href, text in links:
        print(f"  href: {href:<55} text: {text.strip()[:40]}")
