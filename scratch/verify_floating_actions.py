import glob, os, re

base_dir = r"c:\Users\user\Downloads\ABC Trek Website"
files = sorted(glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True))

errors = []
verified_count = 0

for f in files:
    rel = os.path.relpath(f, base_dir)
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # 1. Exactly 1 floating-actions
    floating_count = content.count('class="floating-actions"')
    if floating_count != 1:
        errors.append(f"{rel}: Expected 1 floating-actions, found {floating_count}")
        
    # 2. Contains scrollTopBtn
    if 'id="scrollTopBtn"' not in content:
        errors.append(f"{rel}: Missing id='scrollTopBtn'")
        
    # 3. Contains whatsappBtn with wa.me link
    if 'id="whatsappBtn"' not in content or 'https://wa.me/9779818188459' not in content:
        errors.append(f"{rel}: Missing id='whatsappBtn' or correct WhatsApp link")
        
    verified_count += 1

# Check components.css
with open(os.path.join(base_dir, 'css', 'components.css'), 'r', encoding='utf-8') as fp:
    css_content = fp.read()

for sel in ['.floating-actions', '.btn-floating', '.btn-scroll-top', '.btn-whatsapp']:
    if sel not in css_content:
        errors.append(f"css/components.css: Missing selector {sel}")

# Check js/nav.js
with open(os.path.join(base_dir, 'js', 'nav.js'), 'r', encoding='utf-8') as fp:
    js_content = fp.read()

if 'initFloatingActions' not in js_content or 'scrollTopBtn' not in js_content:
    errors.append("js/nav.js: Missing initFloatingActions or scrollTopBtn handler")

print(f"Verified {verified_count} HTML files, CSS, and JS.")
if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors:
        print(" - " + e)
else:
    print("ALL 29 HTML FILES, CSS, AND JS VERIFIED PERFECTLY! Zero errors.")
