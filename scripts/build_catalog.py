import os
from generate_pages import get_megamenu_html
from run_generation import treks_data

# Category metadata
categories = [
    {
        "id": "abc-treks",
        "name": "Annapurna Base Camp (ABC) Treks",
        "desc": "Expeditions into the natural high-altitude glacial amphitheater beneath Annapurna I (8,091m).",
        "slugs": ["annapurna-base-camp-classic-10-days", "8-days-annapurna-base-camp-trek", "short-annapurna-base-camp-trek"]
    },
    {
        "id": "circuit-treks",
        "name": "Annapurna Circuit Treks",
        "desc": "Epic circumnavigations across distinct climate zones and over the 5,416m Thorong La Pass.",
        "slugs": ["annapurna-circuit-trek", "14-days-annapurna-circuit-trek", "annapurna-circuit-short-trek", "annapurna-circuit-with-tilicho-lake-trek"]
    },
    {
        "id": "poonhill-treks",
        "name": "Poon Hill / Ghorepani Treks",
        "desc": "Accessible, family-friendly sunrise treks through ancient rhododendron forests overlooking Dhaulagiri.",
        "slugs": ["ghorepani-poon-hill-trek", "3-days-poon-hill-trek", "4-days-poon-hill-trek", "5-days-poon-hill-trek"]
    },
    {
        "id": "mardi-treks",
        "name": "Mardi Himal Treks",
        "desc": "Stunning high-ridge walks standing directly face-to-face with the sacred peak of Machhapuchhre.",
        "slugs": ["mardi-himal-trek"]
    },
    {
        "id": "remote-treks",
        "name": "Specialized / Remote Treks",
        "desc": "Off-the-beaten-path expeditions to restricted Tibetan borderlands, high ridges, and authentic eco-villages.",
        "slugs": ["nar-phu-valley-trek", "khopra-ridge-trek", "panchase-trek", "sikles-trek"]
    },
    {
        "id": "cultural-treks",
        "name": "Cultural & Pilgrimage Treks",
        "desc": "Spiritual pilgrimages through the world's deepest river gorge to holy Himalayan shrines.",
        "slugs": ["jomsom-muktinath-trek-with-poon-hill"]
    },
    {
        "id": "scenic-treks",
        "name": "Mountain View / Scenic Treks",
        "desc": "Curated panoramic journeys designed for golden-hour landscape photography and leisurely pacing.",
        "slugs": ["annapurna-view-trek"]
    }
]

# Map treks data by slug
trek_map = {t["slug"]: t for t in treks_data}
# Add the 10-day classic manual data
trek_map["annapurna-base-camp-classic-10-days"] = {
    "slug": "annapurna-base-camp-classic-10-days",
    "title": "10-Day Classic Sanctuary (Flagship)",
    "duration": "10 Days / 9 Nights",
    "elevation": "4,130m",
    "grade": "Moderate+",
    "price": "890",
    "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80",
    "lead": "The benchmark high-altitude route with optimal acclimatization, stone staircases, and base camp dawn."
}

# Generate Category Sections HTML
cat_sections_html = ""
for cat in categories:
    cat_sections_html += f"""
    <section id="{cat['id']}" style="margin-bottom: var(--space-64);">
      <div style="border-bottom: 2px solid var(--color-brand-dark); padding-bottom: var(--space-12); margin-bottom: var(--space-24); display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: var(--space-12);">
        <div>
          <span class="eyebrow" style="margin-bottom: 2px;">Trekking Category</span>
          <h2 style="font-size: 1.75rem; margin-bottom: 4px;">{cat['name']}</h2>
          <p style="font-size: var(--text-body-sm); color: var(--color-text-muted); margin-bottom: 0;">{cat['desc']}</p>
        </div>
        <span class="badge-telemetry" style="font-weight: 700; color: var(--color-brand-dark);">{len(cat['slugs'])} Itineraries</span>
      </div>

      <div class="blog-cards-grid">
    """
    for slug in cat["slugs"]:
        t = trek_map.get(slug)
        if not t:
            continue
        cat_sections_html += f"""
        <div class="blog-card">
          <div style="position: relative;">
            <img src="{t['image']}" alt="{t['title']}" class="blog-card-image">
            <span style="position: absolute; top: 12px; right: 12px; background-color: var(--color-brand-dark); color: #FFFFFF; font-size: 0.6875rem; font-weight: 700; text-transform: uppercase; padding: 4px 8px; border-radius: var(--radius-xs);">
              {t['duration']}
            </span>
          </div>
          <div class="blog-card-content">
            <div class="blog-meta-row">
              <span class="badge-telemetry">{t['elevation']}</span>
              <span class="badge-telemetry">{t['grade']}</span>
            </div>
            <h3 class="blog-card-title" style="font-size: 1.2rem;">
              <a href="{t['slug']}.html">{t['title']}</a>
            </h3>
            <p class="blog-card-excerpt" style="font-size: var(--text-caption);">{t['lead']}</p>
            <div style="margin-top: auto; padding-top: var(--space-12); border-top: 1px solid var(--color-border-subtle); display: flex; justify-content: space-between; align-items: center;">
              <div>
                <span style="font-size: 0.6875rem; color: var(--color-text-muted); display: block;">Starting From</span>
                <span style="font-size: 1.25rem; font-weight: 800; color: var(--color-brand-dark);">${t['price']} <span style="font-size: var(--text-caption); font-weight: normal;">USD</span></span>
              </div>
              <a href="{t['slug']}.html" class="btn btn-primary btn-sm">View Route</a>
            </div>
          </div>
        </div>
        """
    cat_sections_html += "</div></section>"

# Build full treks/index.html
catalog_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>All Annapurna Treks & Routes Directory | ABC Trek in Nepal</title>
  <meta name="description" content="Complete portfolio of Annapurna Base Camp, Annapurna Circuit, Poon Hill, Mardi Himal, and remote wilderness treks in Nepal. Operated by licensed local experts.">
  <link rel="canonical" href="https://abctrekinnepal.com/treks/">
  
  <link rel="stylesheet" href="../css/design-system.css">
  <link rel="stylesheet" href="../css/components.css">
  <style>
    .cat-nav-strip {{
      display: flex;
      gap: var(--space-8);
      overflow-x: auto;
      padding: var(--space-16) 0;
      scrollbar-width: none;
    }}
    .cat-pill {{
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--color-border-subtle);
      background: var(--color-surface-pure);
      font-size: var(--text-body-sm);
      font-weight: 600;
      color: var(--color-brand-dark);
      text-decoration: none;
      white-space: nowrap;
      transition: all var(--transition-fast);
    }}
    .cat-pill:hover {{
      border-color: var(--color-accent);
      color: var(--color-accent);
    }}
  </style>
</head>
<body>

  <!-- Top Announcement Bar -->
  <div class="announcement-bar">
    <div class="container announcement-inner">
      <div class="announcement-left">
        <span class="announcement-badge">Annapurna Portfolio</span>
        <span>All 7 Expedition Categories · 18 Specialized Himalayan Itineraries</span>
      </div>
      <div class="announcement-right">
        <a href="https://wa.me/" class="announcement-link" style="color: #4ADE80; font-weight: 600;">
          WhatsApp Concierge: +977 980 000 0000
        </a>
      </div>
    </div>
  </div>

  <!-- Header with Category Mega-Menu -->
  <header class="site-header">
    <div class="container">
      <div class="header-inner">
        <a href="../index.html" class="brand-logo">
          <svg class="logo-symbol" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M18 4L4 28H32L18 4Z" stroke="#0F2D5C" stroke-width="2.5" stroke-linejoin="round"/>
            <path d="M18 12L10 28H26L18 12Z" fill="#F97316"/>
            <path d="M18 18L14 28H22L18 18Z" fill="#FFFFFF"/>
          </svg>
          <div class="brand-title-wrap">
            <span class="brand-name">ABC TREK</span>
            <span class="brand-tagline">IN NEPAL</span>
          </div>
        </a>

        <nav class="desktop-nav" aria-label="Primary Navigation">
          {get_megamenu_html("sub")}
          <div class="nav-item">
            <a href="../guide/annapurna-base-camp-trek-ultimate-guide.html" class="nav-link">Trek Planning</a>
          </div>
          <div class="nav-item">
            <a href="../safety-ethics/high-altitude-medical-protocols-evacuation.html" class="nav-link">Safety & Ethics</a>
          </div>
          <div class="nav-item">
            <a href="../company/about-us.html" class="nav-link">About Us</a>
          </div>
          <div class="nav-item">
            <a href="../company/contact.html" class="nav-link">Contact</a>
          </div>
        </nav>

        <div class="header-actions">
          <a href="../plan-your-trek.html" class="btn btn-primary btn-sm">Plan Your Trek</a>
        </div>
      </div>
    </div>
  </header>

  <!-- Breadcrumbs -->
  <div style="background-color: var(--color-surface-subtle); border-bottom: 1px solid var(--color-border-subtle); padding: var(--space-12) 0;">
    <div class="container">
      <div class="breadcrumbs" style="margin-bottom: 0;">
        <a href="../index.html">Home</a>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">All Annapurna Treks</span>
      </div>
    </div>
  </div>

  <!-- Page Header -->
  <div class="section" style="padding: var(--space-48) 0; background-color: var(--color-brand-dark-tint);">
    <div class="container">
      <span class="eyebrow">The Complete Annapurna Portfolio</span>
      <h1 class="font-display-xl" style="margin-bottom: var(--space-16);">Annapurna Trekking Expeditions</h1>
      <p class="lead" style="max-width: 820px; margin-bottom: var(--space-20);">
        Explore our curated portfolio of 18 specialized routes organized by category. From classic Annapurna Base Camp and high-altitude Thorong La crossings to remote Nar Phu valleys and family-friendly Poon Hill sunrises.
      </p>

      <!-- Category Filter Pills -->
      <div class="cat-nav-strip">
        <a href="#abc-treks" class="cat-pill">Base Camp Treks</a>
        <a href="#circuit-treks" class="cat-pill">Circuit Treks</a>
        <a href="#poonhill-treks" class="cat-pill">Poon Hill / Ghorepani</a>
        <a href="#mardi-treks" class="cat-pill">Mardi Himal</a>
        <a href="#remote-treks" class="cat-pill">Remote / Specialized</a>
        <a href="#cultural-treks" class="cat-pill">Cultural & Pilgrimage</a>
        <a href="#scenic-treks" class="cat-pill">Mountain View & Scenic</a>
      </div>
    </div>
  </div>

  <!-- Category-Wise Sections Container -->
  <div class="container section">
    {cat_sections_html}
  </div>

  <!-- Global Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="brand-logo" style="margin-bottom: var(--space-16);">
            <svg class="logo-symbol" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M18 4L4 28H32L18 4Z" stroke="#FFFFFF" stroke-width="2.5" stroke-linejoin="round"/>
              <path d="M18 12L10 28H26L18 12Z" fill="#F97316"/>
            </svg>
            <div class="brand-title-wrap">
              <span class="brand-name" style="color: #FFFFFF;">ABC TREK</span>
              <span class="brand-tagline">IN NEPAL</span>
            </div>
          </div>
          <p style="color: var(--color-border-subtle); font-size: var(--text-body-sm); max-width: 380px;">
            The definitive specialist operator for the Annapurna Base Camp (Sanctuary) Trek. Built on conservative high-altitude safety, licensed local leadership, and ethical Himalayan stewardship.
          </p>
        </div>

        <div>
          <div class="footer-col-title">Signature Treks</div>
          <ul class="footer-links">
            <li><a href="annapurna-base-camp-classic-10-days.html" class="footer-link">10-Day Classic Sanctuary</a></li>
            <li><a href="annapurna-circuit-trek.html" class="footer-link">Annapurna Circuit Trek</a></li>
            <li><a href="ghorepani-poon-hill-trek.html" class="footer-link">Ghorepani Poon Hill Trek</a></li>
            <li><a href="mardi-himal-trek.html" class="footer-link">Mardi Himal Trek</a></li>
            <li><a href="nar-phu-valley-trek.html" class="footer-link">Nar Phu Valley Trek</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-col-title">Trekker Resources</div>
          <ul class="footer-links">
            <li><a href="../guide/annapurna-base-camp-trek-ultimate-guide.html" class="footer-link">Ultimate ABC Guide (2026)</a></li>
            <li><a href="../safety-ethics/high-altitude-medical-protocols-evacuation.html" class="footer-link">Altitude Sickness Science</a></li>
            <li><a href="../guide/annapurna-base-camp-trek-ultimate-guide.html#packing" class="footer-link">Complete Packing Checklist</a></li>
            <li><a href="../guide/annapurna-base-camp-trek-ultimate-guide.html#permits" class="footer-link">2026 ACAP Permits & Rules</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-col-title">Trust & Support</div>
          <ul class="footer-links">
            <li><a href="../safety-ethics/high-altitude-medical-protocols-evacuation.html" class="footer-link">Medical Protocols & Rescue</a></li>
            <li><a href="../company/about-us.html" class="footer-link">About Our Mountain Team</a></li>
            <li><a href="../company/contact.html" class="footer-link">Contact Operations Base</a></li>
            <li><a href="../plan-your-trek.html" class="footer-link">Interactive Trip Builder</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 ABC Trek in Nepal. All rights reserved.</div>
        <div style="display: flex; gap: var(--space-16);">
          <a href="../company/about-us.html" class="footer-link">Privacy Policy</a>
          <a href="../company/about-us.html" class="footer-link">Terms & Conditions</a>
        </div>
      </div>
    </div>
  </footer>

</body>
</html>
"""

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
output_file = os.path.join(ROOT_DIR, "treks", "index.html")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(catalog_html)

print("treks/index.html successfully updated with all 7 categories and 18 itineraries.")
