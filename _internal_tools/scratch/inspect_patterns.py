import glob, os, re

files = sorted(glob.glob('**/*.html', recursive=True))

header_patterns = set()
footer_patterns = set()

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Find all <a ... class="brand-logo" ...>
    header_m = re.findall(r'(<a\s+[^>]*class=["\'][^"\']*brand-logo[^"\']*["\'][^>]*>[\s\S]*?</a>)', content)
    for m in header_m:
        header_patterns.add(m)
        
    # Find all <div ... class="brand-logo" ...>
    footer_m = re.findall(r'(<div\s+[^>]*class=["\'][^"\']*brand-logo[^"\']*["\'][^>]*>[\s\S]*?</div>\s*</div>)', content)
    for m in footer_m:
        footer_patterns.add(m)

print(f"Distinct header brand-logo patterns: {len(header_patterns)}")
for idx, p in enumerate(header_patterns):
    print(f"\n--- Header Pattern {idx+1} ---")
    print(p[:300])

print(f"\nDistinct footer brand-logo patterns: {len(footer_patterns)}")
for idx, p in enumerate(footer_patterns):
    print(f"\n--- Footer Pattern {idx+1} ---")
    print(p[:300])
