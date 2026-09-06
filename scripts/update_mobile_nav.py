import os
import re

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_mobile_drawer_html(prefix):
    return f"""  <!-- Mobile Navigation Drawer -->
  <div class="mobile-drawer-overlay" id="mobileOverlay" aria-hidden="true"></div>
  <div class="mobile-drawer" id="mobileMenu" role="dialog" aria-modal="true" aria-label="Mobile Navigation">
    <div class="mobile-drawer-header">
      <div class="brand-title-wrap">
        <span class="brand-name">ABC TREK</span>
        <span class="brand-tagline">IN NEPAL</span>
      </div>
      <button class="mobile-drawer-close" id="mobileMenuClose" aria-label="Close Navigation Menu">✕</button>
    </div>
    <div class="mobile-drawer-body">
      <ul class="mobile-drawer-links">
        <li><a href="{prefix}index.html" class="mobile-nav-link"><span>Home</span></a></li>
        <li>
          <button class="mobile-nav-link mobile-accordion-toggle" aria-expanded="false">
            <span>Annapurna Treks</span>
            <svg class="accordion-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <ul class="mobile-accordion-panel">
            <li><a href="{prefix}treks/annapurna-base-camp-classic-10-days.html" class="mobile-sub-link"><span>10-Day Sanctuary (Flagship)</span></a></li>
            <li><a href="{prefix}treks/8-days-annapurna-base-camp-trek.html" class="mobile-sub-link"><span>8 Days ABC Trek</span></a></li>
            <li><a href="{prefix}treks/short-annapurna-base-camp-trek.html" class="mobile-sub-link"><span>Short ABC Trek</span></a></li>
            <li><a href="{prefix}treks/annapurna-circuit-trek.html" class="mobile-sub-link"><span>Annapurna Circuit Trek</span></a></li>
            <li><a href="{prefix}treks/14-days-annapurna-circuit-trek.html" class="mobile-sub-link"><span>14 Days Circuit Trek</span></a></li>
            <li><a href="{prefix}treks/ghorepani-poon-hill-trek.html" class="mobile-sub-link"><span>Ghorepani Poon Hill</span></a></li>
            <li><a href="{prefix}treks/3-days-poon-hill-trek.html" class="mobile-sub-link"><span>3 Days Poon Hill</span></a></li>
            <li><a href="{prefix}treks/mardi-himal-trek.html" class="mobile-sub-link"><span>Mardi Himal Ridge</span></a></li>
            <li><a href="{prefix}treks/nar-phu-valley-trek.html" class="mobile-sub-link"><span>Nar Phu Valley</span></a></li>
            <li><a href="{prefix}treks/khopra-ridge-trek.html" class="mobile-sub-link"><span>Khopra Ridge</span></a></li>
            <li><a href="{prefix}treks/index.html" class="mobile-sub-link" style="font-weight: 700; color: var(--color-accent);"><span>View All 18 Treks &rarr;</span></a></li>
          </ul>
        </li>
        <li><a href="{prefix}guide/annapurna-base-camp-trek-ultimate-guide.html" class="mobile-nav-link"><span>Trek Planning Guide</span></a></li>
        <li><a href="{prefix}safety-ethics/high-altitude-medical-protocols-evacuation.html" class="mobile-nav-link"><span>Safety & Ethics</span></a></li>
        <li><a href="{prefix}company/about-us.html" class="mobile-nav-link"><span>About Our Specialists</span></a></li>
        <li><a href="{prefix}company/contact.html" class="mobile-nav-link"><span>Contact Mountain Operations</span></a></li>
      </ul>
    </div>
    <div class="mobile-drawer-footer">
      <a href="{prefix}plan-your-trek.html" class="btn btn-primary" style="width: 100%; text-align: center; justify-content: center;">Plan Your Trek</a>
      <a href="https://wa.me/9779818188459" class="btn btn-secondary" style="width: 100%; text-align: center; justify-content: center; color: #22C55E; border-color: #22C55E;">WhatsApp Concierge</a>
    </div>
  </div>"""

hamburger_btn = """          <button class="mobile-nav-toggle" id="mobileMenuOpen" aria-label="Open Navigation Menu">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="3" y1="6" x2="21" y2="6"></line>
              <line x1="3" y1="12" x2="21" y2="12"></line>
              <line x1="3" y1="18" x2="21" y2="18"></line>
            </svg>
          </button>"""

def update_file(filepath):
    rel_path = os.path.relpath(filepath, ROOT_DIR)
    depth = 0 if os.path.dirname(rel_path) == "" else 1
    prefix = "../" if depth > 0 else ""

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update header-actions to include hamburger button
    if 'id="mobileMenuOpen"' not in content:
        # Match <div class="header-actions">...</div>
        def repl_ha(match):
            inner = match.group(1)
            if 'mobileMenuOpen' not in inner:
                return f'<div class="header-actions">\n{inner.rstrip()}\n{hamburger_btn}\n        </div>'
            return match.group(0)
        content = re.sub(r'<div class="header-actions">(.*?)</div>', repl_ha, content, count=1, flags=re.DOTALL)

    # 2. Update or insert mobile drawer
    new_drawer = get_mobile_drawer_html(prefix)
    if 'id="mobileMenu"' in content:
        # Replace existing mobile drawer and overlay
        content = re.sub(
            r'<!-- Mobile Drawer Menu -->\s*<div class="mobile-drawer-overlay".*?</div>\s*</div>',
            new_drawer,
            content,
            count=1,
            flags=re.DOTALL
        )
        if 'id="mobileMenu"' not in content or 'mobile-accordion-toggle' not in content:
            # Fallback regex if comment format differed
            content = re.sub(
                r'<div class="mobile-drawer-overlay".*?</div>\s*</div>',
                new_drawer,
                content,
                count=1,
                flags=re.DOTALL
            )
    else:
        # Insert after </header>
        content = content.replace('</header>', f'</header>\n\n{new_drawer}', 1)

    # 3. Clean up old inline mobile toggle scripts if present
    content = re.sub(
        r'<!-- Mobile Drawer Toggle Script -->\s*<script>.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )

    # 4. Ensure js/nav.js is linked before </body>
    script_tag = f'<script src="{prefix}js/nav.js" defer></script>'
    if script_tag not in content:
        content = content.replace('</body>', f'  {script_tag}\n</body>', 1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated: {rel_path}")

def run():
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        # Skip docs and scripts directories
        if os.path.basename(root) in ["docs", "scripts", "__pycache__", ".git"]:
            continue
        for file in files:
            if file.endswith(".html"):
                update_file(os.path.join(root, file))
                count += 1
    print(f"\nSuccessfully standardized mobile navigation across {count} HTML pages.")

if __name__ == "__main__":
    run()
