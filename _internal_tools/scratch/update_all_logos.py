import glob, os, re

base_dir = r"c:\Users\user\Downloads\ABC Trek Website"
files = sorted(glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True))

svg_pattern = re.compile(r'<svg[^>]*class=["\'][^"\']*logo-symbol[^"\']*["\'][^>]*>[\s\S]*?</svg>')

updated_files = 0
total_replacements = 0

for f in files:
    rel_path = os.path.relpath(f, base_dir)
    is_sub = ("\\" in rel_path) or ("/" in rel_path)
    img_src = "../images/logo.png" if is_sub else "images/logo.png"
    img_tag = f'<img src="{img_src}" alt="ABC Trek in Nepal Logo" class="brand-logo-img">'
    
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    matches = list(svg_pattern.finditer(content))
    if not matches:
        print(f"Skipping {rel_path} (0 matches, already updated or none)")
        continue
    
    new_content = svg_pattern.sub(img_tag, content)
    
    with open(f, "w", encoding="utf-8") as fp:
        fp.write(new_content)
    
    updated_files += 1
    total_replacements += len(matches)
    print(f"Updated {rel_path}: replaced {len(matches)} SVGs with '{img_src}'")

print("-" * 60)
print(f"Total files updated: {updated_files}")
print(f"Total SVGs replaced: {total_replacements}")
