import glob, os, re

files = sorted(glob.glob('**/*.html', recursive=True))

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Find all svg with class logo-symbol
    svgs = re.findall(r'<svg[^>]*class=["\'][^"\']*logo-symbol[^"\']*["\'][^>]*>[\s\S]*?</svg>', content)
    print(f"{f:<50}: {len(svgs)} svgs found")
