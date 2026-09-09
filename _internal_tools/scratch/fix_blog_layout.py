import glob
import re
import os

# 1. Update css/components.css to enforce strict !important dimensions
components_path = 'css/components.css'
with open(components_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace .brand-logo-img definition
old_logo_rule = """.logo-symbol,
.brand-logo-img {
  width: 44px;
  height: 44px;
  object-fit: contain;
  display: block;
  flex-shrink: 0;
  border-radius: 50%;
  transition: transform var(--transition-base, 0.2s ease);
}"""

new_logo_rule = """.logo-symbol,
.brand-logo-img {
  width: 44px !important;
  height: 44px !important;
  max-width: 44px !important;
  max-height: 44px !important;
  object-fit: contain !important;
  display: block !important;
  flex-shrink: 0 !important;
  border-radius: 50% !important;
  transition: transform var(--transition-base, 0.2s ease);
}"""

if old_logo_rule in css_content:
    css_content = css_content.replace(old_logo_rule, new_logo_rule)
    print("Enforced !important on brand-logo-img in components.css")

# Also ensure .blog-search-icon has !important
old_search_icon = """.blog-search-icon {
  position: absolute;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
  color: var(--color-text-muted);
  pointer-events: none;
}"""

new_search_icon = """.blog-search-icon {
  position: absolute;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  width: 20px !important;
  height: 20px !important;
  max-width: 20px !important;
  max-height: 20px !important;
  color: var(--color-text-muted);
  pointer-events: none;
  flex-shrink: 0;
}"""

if old_search_icon in css_content:
    css_content = css_content.replace(old_search_icon, new_search_icon)
    print("Enforced !important on blog-search-icon in components.css")

with open(components_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Add baseline rule to design-system.css as fail-safe
ds_path = 'css/design-system.css'
with open(ds_path, 'r', encoding='utf-8') as f:
    ds_content = f.read()

if '.brand-logo-img {' not in ds_content:
    ds_content += "\n/* Fail-safe logo dimensions */\n.brand-logo-img { width: 44px !important; height: 44px !important; max-width: 44px !important; max-height: 44px !important; object-fit: contain; border-radius: 50%; display: block; }\n"
    with open(ds_path, 'w', encoding='utf-8') as f:
        f.write(ds_content)
    print("Added fail-safe rule to design-system.css")

# 3. Update all HTML files:
#    - Add inline width="44" height="44" to every brand-logo-img
#    - Update CSS version cache buster to ?v=2.3
html_files = glob.glob('**/*.html', recursive=True)
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content
    # Update logo tags: add width="44" height="44" and inline style
    def logo_replacer(match):
        tag = match.group(0)
        if 'width=' in tag and 'height=' in tag:
            return tag
        # Insert width, height and style before closing >
        tag = re.sub(r'>$', ' width="44" height="44" style="width: 44px; height: 44px; object-fit: contain; border-radius: 50%; display: block;">', tag)
        return tag

    content = re.sub(r'<img[^>]*class=[\"\'][^\"\']*brand-logo-img[^\"\']*[\"\'][^>]*>', logo_replacer, content)

    # In blog.html specifically, constrain the search icon and featured visual SVG
    if os.path.basename(hf) == 'blog.html':
        content = content.replace(
            '<svg class="blog-search-icon" viewBox="0 0 24 24"',
            '<svg class="blog-search-icon" width="20" height="20" viewBox="0 0 24 24" style="width: 20px; height: 20px; min-width: 20px;"'
        )
        content = content.replace(
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="12 2 2 22 22 22 12 2"></polygon></svg>',
            '<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width: 64px; height: 64px;"><polygon points="12 2 2 22 22 22 12 2"></polygon></svg>'
        )

    # Cache buster bump to v=2.3 across all files
    content = re.sub(r'design-system\.css(\?v=[0-9\.]+)?', 'design-system.css?v=2.3', content)
    content = re.sub(r'components\.css(\?v=[0-9\.]+)?', 'components.css?v=2.3', content)

    if content != orig:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML: {hf}")

print("Fix completed!")
