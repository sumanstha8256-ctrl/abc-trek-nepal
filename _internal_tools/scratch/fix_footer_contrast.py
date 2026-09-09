import glob
import re
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 1. Update css/components.css
components_path = os.path.join(ROOT_DIR, 'css/components.css')
with open(components_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace footer-link rule to include .footer-links a and .site-footer a
old_footer_rule = """.footer-link {
  color: var(--color-text-inverse-muted);
  text-decoration: none;
  font-size: var(--text-body-sm);
  transition: color var(--transition-fast);
}

.footer-link:hover {
  color: var(--color-accent);
}"""

new_footer_rule = """.footer-links a,
.footer-link,
.site-footer a:not(.btn):not(.brand-logo) {
  color: #CBD5E1 !important;
  text-decoration: none;
  font-size: var(--text-body-sm);
  transition: color var(--transition-fast);
}

.footer-links a:hover,
.footer-link:hover,
.site-footer a:not(.btn):not(.brand-logo):hover {
  color: #F97316 !important;
}"""

if old_footer_rule in css:
    css = css.replace(old_footer_rule, new_footer_rule)
    print("Updated footer link rules in css/components.css")
else:
    # Append if exact block not found
    css += "\n\n/* High Contrast Footer Links */\n" + new_footer_rule + "\n"
    print("Appended high contrast footer rules to css/components.css")

with open(components_path, 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update css/design-system.css with global fallback
ds_path = os.path.join(ROOT_DIR, 'css/design-system.css')
with open(ds_path, 'r', encoding='utf-8') as f:
    ds = f.read()

fallback_rule = "\n/* High contrast footer links fallback */\n.site-footer a { color: #CBD5E1; }\n.site-footer a:hover { color: #F97316; }\n"
if 'High contrast footer links fallback' not in ds:
    ds += fallback_rule
    with open(ds_path, 'w', encoding='utf-8') as f:
        f.write(ds)
    print("Added fallback to css/design-system.css")

# 3. Add class="footer-link" to all <a> inside .footer-links in all HTML files
# and bump cache buster to ?v=2.4
html_files = glob.glob(os.path.join(ROOT_DIR, '**/*.html'), recursive=True)

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # Add class="footer-link" to any <a> inside <ul class="footer-links"> that lacks it
    def add_footer_class(match):
        ul_content = match.group(0)
        def link_sub(a_match):
            a_tag = a_match.group(0)
            if 'class=' in a_tag:
                return a_tag
            return a_tag.replace('<a ', '<a class="footer-link" ')
        return re.sub(r'<a\s+[^>]*>', link_sub, ul_content)

    content = re.sub(r'<ul class=[\"\']footer-links[\"\']>.*?</ul>', add_footer_class, content, flags=re.DOTALL)

    # Bump cache buster to ?v=2.4
    content = re.sub(r'design-system\.css\?v=[0-9\.]+', 'design-system.css?v=2.4', content)
    content = re.sub(r'components\.css\?v=[0-9\.]+', 'components.css?v=2.4', content)
    content = re.sub(r'nav\.js\?v=[0-9\.]+', 'nav.js?v=2.4', content)

    if content != orig:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated footer links & v=2.4 in: {os.path.basename(hf)}")

print("Footer link contrast fix complete!")
