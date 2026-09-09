import glob, os, re

base_dir = r"c:\Users\user\Downloads\ABC Trek Website"
files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

print(f"Total HTML files found: {len(files)}")

patterns = [
    re.compile(r'<a\s+[^>]*class=["\'][^"\']*brand-logo[^"\']*["\'][^>]*>(.*?)</a>', re.DOTALL | re.IGNORECASE),
    re.compile(r'<div\s+[^>]*class=["\'][^"\']*brand-logo[^"\']*["\'][^>]*>(.*?)</div>\s*</div>', re.DOTALL | re.IGNORECASE),
]

results = []

for f in sorted(files):
    rel = os.path.relpath(f, base_dir)
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    brand_logo_count = content.count("brand-logo")
    logo_symbol_count = content.count("logo-symbol")
    results.append((rel, brand_logo_count, logo_symbol_count))

print(f"{'File':<45} | {'brand-logo':<12} | {'logo-symbol':<12}")
print("-" * 75)
for r in results:
    print(f"{r[0]:<45} | {r[1]:<12} | {r[2]:<12}")
