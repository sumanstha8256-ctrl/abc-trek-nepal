import re

scripts = ['scripts/generate_pages.py', 'scripts/build_catalog.py']
for s in scripts:
    with open(s, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'href=([\"\'])([^\"\']*)\.html([#\?][^\"\']*)?\1', r'href=\1\2\3\1', c)
    c = re.sub(r'https://abctrekinnepal\.com/([^\"\']+)\.html', r'https://abctrekinnepal.com/\1', c)
    with open(s, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Cleaned {s}")
