import os
from generate_pages import get_megamenu_html

# 1. Update index.html with the root-level mega menu
root_megamenu = get_megamenu_html("root")
sub_megamenu = get_megamenu_html("sub")

def update_file_nav(filepath, megamenu_code):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Locate <nav class="desktop-nav"...>
    start_tag = '<nav class="desktop-nav"'
    if start_tag in content:
        start_idx = content.find(start_tag)
        end_idx = content.find('</nav>', start_idx)
        if end_idx != -1:
            # We want to replace the first <div class="nav-item">...</div> with our mega-menu
            # Or rebuild the desktop-nav content cleanly
            prefix = "" if "root" in megamenu_code else "../"
            new_nav = f"""<nav class="desktop-nav" aria-label="Primary Navigation">
          {megamenu_code}
          <div class="nav-item">
            <a href="{prefix}guide/annapurna-base-camp-trek-ultimate-guide.html" class="nav-link">Trek Planning</a>
          </div>
          <div class="nav-item">
            <a href="{prefix}safety-ethics/high-altitude-medical-protocols-evacuation.html" class="nav-link">Safety & Ethics</a>
          </div>
          <div class="nav-item">
            <a href="{prefix}company/about-us.html" class="nav-link">About Us</a>
          </div>
          <div class="nav-item">
            <a href="{prefix}company/contact.html" class="nav-link">Contact</a>
          </div>
        </nav>"""
            content = content[:start_idx] + new_nav + content[end_idx+6:]
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated nav in {filepath}")

# Update root files
update_file_nav("c:/Users/user/Downloads/ABC Trek Website/index.html", root_megamenu)
update_file_nav("c:/Users/user/Downloads/ABC Trek Website/plan-your-trek.html", root_megamenu)

# Update subfolder files
update_file_nav("c:/Users/user/Downloads/ABC Trek Website/treks/annapurna-base-camp-classic-10-days.html", sub_megamenu)
update_file_nav("c:/Users/user/Downloads/ABC Trek Website/guide/annapurna-base-camp-trek-ultimate-guide.html", sub_megamenu)
update_file_nav("c:/Users/user/Downloads/ABC Trek Website/safety-ethics/high-altitude-medical-protocols-evacuation.html", sub_megamenu)
update_file_nav("c:/Users/user/Downloads/ABC Trek Website/company/about-us.html", sub_megamenu)
update_file_nav("c:/Users/user/Downloads/ABC Trek Website/company/contact.html", sub_megamenu)

print("Nav menus updated successfully.")
