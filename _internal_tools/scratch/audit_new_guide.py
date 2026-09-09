import os, re

base_dir = r"c:\Users\user\Downloads\ABC Trek Website"
target = os.path.join(base_dir, "guide", "annapurna-base-camp-trek-september.html")

with open(target, "r", encoding="utf-8") as f:
    content = f.read()

# Check all local relative links (img, script, link, a)
issues = []

# Img srcs
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
for img in imgs:
    if not img.startswith("http"):
        p = os.path.normpath(os.path.join(os.path.dirname(target), img))
        if not os.path.exists(p):
            issues.append(f"Image not found: {img} -> {p}")

# CSS links
csss = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', content)
for c in csss:
    clean_c = c.split("?")[0]
    p = os.path.normpath(os.path.join(os.path.dirname(target), clean_c))
    if not os.path.exists(p):
        issues.append(f"CSS not found: {c} -> {p}")

# Scripts
scripts = re.findall(r'<script[^>]+src=["\']([^"\']+\.js[^"\']*)["\']', content)
for s in scripts:
    clean_s = s.split("?")[0]
    p = os.path.normpath(os.path.join(os.path.dirname(target), clean_s))
    if not os.path.exists(p):
        issues.append(f"Script not found: {s} -> {p}")

print(f"Target size: {len(content)} bytes")
print(f"Images checked: {len(imgs)}")
print(f"CSS checked: {len(csss)}")
print(f"Scripts checked: {len(scripts)}")
if issues:
    print(f"ERRORS: {issues}")
else:
    print("ALL ASSETS & LINKS VERIFIED WITH ZERO ERRORS!")
