import glob, os, re

files = sorted(glob.glob('**/*.html', recursive=True))

for f in files:
    if f == 'index.html':
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    matches = list(re.finditer(r'<svg[^>]*class=["\'][^"\']*logo-symbol[^"\']*["\'][^>]*>[\s\S]*?</svg>', content))
    if len(matches) != 2:
        print(f"WARNING: {f} has {len(matches)} matches!")
    else:
        print(f"{f}: OK (2 SVGs)")
