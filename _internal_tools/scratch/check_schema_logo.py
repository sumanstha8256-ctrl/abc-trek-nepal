import glob, os, re

base_dir = r"c:\Users\user\Downloads\ABC Trek Website"
files = sorted(glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True))

for f in files:
    rel_path = os.path.relpath(f, base_dir)
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    # Check if "logo" is mentioned in script json or meta tags
    matches = re.findall(r'(\"logo\"[^\n,}]+)', content)
    favicons = re.findall(r'<link[^>]*rel=["\'][^"\']*icon[^"\']*["\'][^>]*>', content)
    og_images = re.findall(r'<meta[^>]*property=["\']og:image["\'][^>]*>', content)
    if matches or favicons:
        print(f"{rel_path}:")
        if matches:
            print("  schema logo:", matches)
        if favicons:
            print("  favicon:", favicons)
