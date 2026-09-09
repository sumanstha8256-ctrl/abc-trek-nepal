import glob
import re
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 1. Update CSS components.css with strict dimensions
components_path = os.path.join(ROOT_DIR, 'css/components.css')
with open(components_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure .blog-featured-visual svg has strict constraints
featured_svg_old = """.blog-featured-visual svg {
  width: 64px;
  height: 64px;
  opacity: 0.9;
  margin-bottom: var(--space-12);
}"""

featured_svg_new = """.blog-featured-visual svg {
  width: 64px !important;
  height: 64px !important;
  max-width: 64px !important;
  max-height: 64px !important;
  opacity: 0.9;
  margin-bottom: var(--space-12);
  display: block;
}"""

if featured_svg_old in css:
    css = css.replace(featured_svg_old, featured_svg_new)

with open(components_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated css/components.css")

# 2. Update all HTML files to use ROOT-RELATIVE asset paths (/css/..., /js/..., /images/...)
html_files = glob.glob(os.path.join(ROOT_DIR, '**/*.html'), recursive=True)

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # 1. Root-relative CSS links with ?v=2.3
    content = re.sub(r'href=[\"\'](\.\./)?css/design-system\.css(\?v=[0-9\.]+)?[\"\']', 'href="/css/design-system.css?v=2.3"', content)
    content = re.sub(r'href=[\"\'](\.\./)?css/components\.css(\?v=[0-9\.]+)?[\"\']', 'href="/css/components.css?v=2.3"', content)

    # 2. Root-relative JS links with ?v=2.3
    content = re.sub(r'src=[\"\'](\.\./)?js/nav\.js(\?v=[0-9\.]+)?[\"\']', 'src="/js/nav.js?v=2.3"', content)

    # 3. Root-relative images
    content = re.sub(r'src=[\"\'](\.\./)?images/', 'src="/images/', content)
    content = re.sub(r'href=[\"\'](\.\./)?images/', 'href="/images/', content)

    # 4. In blog.html, add inline dimensions to SVGs and logo img
    if os.path.basename(hf) == 'blog.html':
        content = re.sub(
            r'<svg class=[\"\']blog-search-icon[\"\'][^>]*>',
            '<svg class="blog-search-icon" width="20" height="20" viewBox="0 0 24 24" style="width: 20px !important; height: 20px !important; min-width: 20px; flex-shrink: 0;" fill="none" stroke="currentColor" stroke-width="2.5">',
            content
        )
        content = re.sub(
            r'<svg width=[\"\']64[\"\'][^>]*polygon[^>]*></svg>',
            '<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width: 64px !important; height: 64px !important; max-width: 64px; max-height: 64px;"><polygon points="12 2 2 22 22 22 12 2"></polygon></svg>',
            content
        )
        content = content.replace(
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="12 2 2 22 22 22 12 2"></polygon></svg>',
            '<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="width: 64px !important; height: 64px !important; max-width: 64px; max-height: 64px;"><polygon points="12 2 2 22 22 22 12 2"></polygon></svg>'
        )

    # 5. Make sure logo img has inline width, height and style
    def logo_fixer(match):
        tag = match.group(0)
        # remove old width/height/style if any to normalize
        tag_clean = re.sub(r'\s+(width|height|style)=[\"\'][^\"\']*[\"\']', '', tag)
        tag_clean = tag_clean.rstrip('>').rstrip('/') + ' width="44" height="44" style="width: 44px !important; height: 44px !important; max-width: 44px !important; max-height: 44px !important; object-fit: contain; border-radius: 50%; display: block;">'
        return tag_clean

    content = re.sub(r'<img[^>]*class=[\"\'][^\"\']*brand-logo-img[^\"\']*[\"\'][^>]*>', logo_fixer, content)

    if content != orig:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated root-relative assets in: {os.path.basename(hf)}")

print("All asset paths normalized to root-relative!")
