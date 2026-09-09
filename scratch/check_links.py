import glob, os, re

files = glob.glob('**/*.html', recursive=True)

for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    # Check css links
    css_links = re.findall(r'<link[^>]*href=["\']([^"\']+\.css)["\']', content)
    # Check img links
    img_links = re.findall(r'<img[^>]*src=["\']([^"\']+)["\']', content)
    print(f"{f}:")
    print(f"  CSS: {css_links[:2]}")
    if img_links:
        print(f"  IMG: {img_links[:2]}")
