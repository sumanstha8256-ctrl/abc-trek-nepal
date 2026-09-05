import re
import os
import glob

print("Starting business details enhancement...")

# Define the standard footer credentials block based on relative path
def get_footer_block(depth=0):
    rel_prefix = "../" if depth > 0 else ""
    return f'''          <p style="color: var(--color-border-subtle); font-size: var(--text-body-sm); max-width: 380px; line-height: 1.6;">
            The definitive specialist operator for the Annapurna Base Camp (Sanctuary) Trek. Built on conservative high-altitude safety, licensed local leadership, and ethical Himalayan stewardship.
          </p>
          <div style="font-size: var(--text-caption); color: var(--color-text-inverse-muted); margin-top: var(--space-16); line-height: 1.7;">
            <div><strong>Founder & Expedition Lead:</strong> Suman Shrestha</div>
            <div><strong>Kathmandu Hub:</strong> Budhanilkantha, Kathmandu, Nepal</div>
            <div><strong>Operations Base:</strong> Lakeside-6, Pokhara, Nepal</div>
            <div><strong>Direct Phone:</strong> <a href="tel:+9779818188459" style="color: #FFFFFF; text-decoration: underline;">+977 9818188459</a></div>
            <div><strong>WhatsApp Concierge:</strong> <a href="https://wa.me/9779818188459" target="_blank" rel="noopener" style="color: #4ADE80; font-weight: 600; text-decoration: underline;">+977 9818188459</a></div>
          </div>'''

# Process all html files to standardize the footer block
files = glob.glob('**/*.html', recursive=True)
print(f"Found {len(files)} HTML files to update.")

for f in files:
    depth = 1 if ('/' in f.replace('\\', '/') and not f.startswith('./')) else 0
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Standardize footer col 1
    # Find the brand description paragraph in the footer
    pattern = r'<p style="color: var\(--color-border-subtle\); font-size: var\(--text-body-sm\); max-width: 380px;.*?</p>(\s*<div style="font-size: var\(--text-caption\);.*?</div\s*>)?'
    replacement = get_footer_block(depth)
    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    
    if count > 0:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        print(f"Updated footer in {f}")
    else:
        print(f"Footer pattern not matched in {f}")

print("Footer standardization complete.")
