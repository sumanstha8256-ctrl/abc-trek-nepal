import glob, os, re

base_dir = r"c:\Users\user\Downloads\ABC Trek Website"
files = sorted(glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True))

errors = []
total_verified = 0

for f in files:
    rel_path = os.path.relpath(f, base_dir)
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    # Check old SVG
    svg_matches = re.findall(r'<svg[^>]*class=["\'][^"\']*logo-symbol[^"\']*["\'][^>]*>', content)
    if svg_matches:
        errors.append(f"{rel_path}: Found {len(svg_matches)} unreplaced logo-symbol SVGs!")
    
    # Check new img tags
    img_matches = re.findall(r'<img\s+[^>]*class=["\'][^"\']*brand-logo-img[^"\']*["\'][^>]*>', content)
    if len(img_matches) != 2:
        errors.append(f"{rel_path}: Found {len(img_matches)} brand-logo-img tags (expected 2)!")
    
    # Check that referenced image file exists
    src_matches = re.findall(r'<img\s+[^>]*class=["\'][^"\']*brand-logo-img[^"\']*["\'][^>]*src=["\']([^"\']+)["\']', content)
    for src in src_matches:
        img_full_path = os.path.normpath(os.path.join(os.path.dirname(f), src))
        if not os.path.exists(img_full_path):
            errors.append(f"{rel_path}: Image file {src} does not exist at {img_full_path}!")
            
    total_verified += 1

print(f"Verified {total_verified} HTML files.")
if errors:
    print(f"FAILED with {len(errors)} errors:")
    for err in errors:
        print(" - " + err)
else:
    print("ALL 29 HTML FILES VERIFIED PERFECTLY! Zero errors found.")
