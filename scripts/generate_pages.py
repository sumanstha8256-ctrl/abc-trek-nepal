import os

# Define the complete category-wise mega menu HTML snippet (for root and subfolders)
def get_megamenu_html(depth="sub"):
    prefix = "../" if depth == "sub" else ""
    return f"""<!-- Dropdown 1: Annapurna Treks Mega-Menu -->
          <div class="nav-item">
            <a href="{prefix}treks/index" class="nav-link active">
              <span>Annapurna Treks</span>
              <svg class="nav-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </a>
            <div class="nav-megamenu">
              <div class="megamenu-grid">
                <!-- Col 1: ABC & Circuit -->
                <div class="megamenu-col">
                  <div class="megamenu-category-header">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 4L4 28H32L18 4Z"/></svg>
                    <span>Annapurna Base Camp</span>
                  </div>
                  <ul class="megamenu-list">
                    <li><a href="{prefix}treks/annapurna-base-camp-classic-10-days" class="megamenu-link"><span>10-Day Classic Sanctuary</span><span class="megamenu-badge">Flagship</span></a></li>
                    <li><a href="{prefix}treks/8-days-annapurna-base-camp-trek" class="megamenu-link"><span>8 Days ABC Trek</span><span class="megamenu-badge">8 Days</span></a></li>
                    <li><a href="{prefix}treks/short-annapurna-base-camp-trek" class="megamenu-link"><span>Short ABC Trek</span><span class="megamenu-badge">Express</span></a></li>
                  </ul>

                  <div class="megamenu-category-header" style="margin-top: var(--space-16);">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle></svg>
                    <span>Annapurna Circuit</span>
                  </div>
                  <ul class="megamenu-list">
                    <li><a href="{prefix}treks/annapurna-circuit-trek" class="megamenu-link"><span>Annapurna Circuit Trek</span><span class="megamenu-badge">Classic</span></a></li>
                    <li><a href="{prefix}treks/14-days-annapurna-circuit-trek" class="megamenu-link"><span>14 Days Circuit Trek</span><span class="megamenu-badge">14 Days</span></a></li>
                    <li><a href="{prefix}treks/annapurna-circuit-short-trek" class="megamenu-link"><span>Short Circuit Trek</span><span class="megamenu-badge">10 Days</span></a></li>
                    <li><a href="{prefix}treks/annapurna-circuit-with-tilicho-lake-trek" class="megamenu-link"><span>Circuit with Tilicho Lake</span><span class="megamenu-badge">4,919m</span></a></li>
                  </ul>
                </div>

                <!-- Col 2: Poon Hill & Mardi -->
                <div class="megamenu-col">
                  <div class="megamenu-category-header">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>
                    <span>Poon Hill / Ghorepani</span>
                  </div>
                  <ul class="megamenu-list">
                    <li><a href="{prefix}treks/ghorepani-poon-hill-trek" class="megamenu-link"><span>Ghorepani Poonhill Trek</span><span class="megamenu-badge">Popular</span></a></li>
                    <li><a href="{prefix}treks/3-days-poon-hill-trek" class="megamenu-link"><span>3 Days PoonHill Trek</span><span class="megamenu-badge">3 Days</span></a></li>
                    <li><a href="{prefix}treks/4-days-poon-hill-trek" class="megamenu-link"><span>4 Days PoonHill Trek</span><span class="megamenu-badge">4 Days</span></a></li>
                    <li><a href="{prefix}treks/5-days-poon-hill-trek" class="megamenu-link"><span>5 Day PoonHill Trek</span><span class="megamenu-badge">5 Days</span></a></li>
                  </ul>

                  <div class="megamenu-category-header" style="margin-top: var(--space-16);">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
                    <span>Mardi Himal</span>
                  </div>
                  <ul class="megamenu-list">
                    <li><a href="{prefix}treks/mardi-himal-trek" class="megamenu-link"><span>Mardi Himal Trek</span><span class="megamenu-badge">Ridge Trek</span></a></li>
                  </ul>
                </div>

                <!-- Col 3: Specialized & Remote -->
                <div class="megamenu-col">
                  <div class="megamenu-category-header">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
                    <span>Specialized & Remote</span>
                  </div>
                  <ul class="megamenu-list">
                    <li><a href="{prefix}treks/nar-phu-valley-trek" class="megamenu-link"><span>Nar Phu Valley Trek</span><span class="megamenu-badge">Restricted</span></a></li>
                    <li><a href="{prefix}treks/khopra-ridge-trek" class="megamenu-link"><span>Khopra Ridge Trek</span><span class="megamenu-badge">Panoramic</span></a></li>
                    <li><a href="{prefix}treks/panchase-trek" class="megamenu-link"><span>Panchase Trek</span><span class="megamenu-badge">Eco-Walk</span></a></li>
                    <li><a href="{prefix}treks/sikles-trek" class="megamenu-link"><span>Sikles Trek</span><span class="megamenu-badge">Gurung Lore</span></a></li>
                  </ul>
                </div>

                <!-- Col 4: Cultural & Scenic -->
                <div class="megamenu-col">
                  <div class="megamenu-category-header">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2a8 8 0 0 0-8 8c0 5 8 12 8 12s8-7 8-12a8 8 0 0 0-8-8zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
                    <span>Cultural & Pilgrimage</span>
                  </div>
                  <ul class="megamenu-list">
                    <li><a href="{prefix}treks/jomsom-muktinath-trek-with-poon-hill" class="megamenu-link"><span>Jomsom Muktinath Trek</span><span class="megamenu-badge">Pilgrimage</span></a></li>
                  </ul>

                  <div class="megamenu-category-header" style="margin-top: var(--space-16);">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/></svg>
                    <span>Mountain View & Scenic</span>
                  </div>
                  <ul class="megamenu-list">
                    <li><a href="{prefix}treks/annapurna-view-trek" class="megamenu-link"><span>Annapurna View Trek</span><span class="megamenu-badge">Scenic</span></a></li>
                  </ul>
                </div>
              </div>

              <!-- Megamenu Footer -->
              <div class="megamenu-footer">
                <span>Looking for tailor-made group pacing?</span>
                <a href="{prefix}plan-your-trek" style="color: var(--color-accent); font-weight: 700;">Explore Custom Departures &rarr;</a>
              </div>
            </div>
          </div>"""

# Template for generating individual trek pages
def generate_trek_page(trek):
    slug = trek["slug"]
    title = trek["title"]
    category = trek["category"]
    duration = trek["duration"]
    elevation = trek["elevation"]
    grade = trek["grade"]
    price = trek["price"]
    image = trek["image"]
    headline = trek["headline"]
    lead = trek["lead"]
    overview = trek["overview"]
    highlights = trek["highlights"]
    itinerary_days = trek["itinerary"]
    faqs = trek["faqs"]

    # Build Highlights HTML
    hl_html = "".join([f"""<div class="fact-tile">
      <svg class="fact-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
      <div class="fact-title">{h[0]}</div>
      <p style="font-size: var(--text-caption); color: var(--color-text-muted); margin-bottom: 0;">{h[1]}</p>
    </div>""" for h in highlights])

    # Build Itinerary HTML
    itin_html = ""
    for idx, day in enumerate(itinerary_days):
        open_cls = "open" if idx == 0 else ""
        itin_html += f"""<div class="itinerary-day {open_cls}">
          <button class="itinerary-trigger" onclick="this.parentElement.classList.toggle('open')">
            <div>
              <span class="day-index">Day {idx+1:02d}</span>
              <span class="day-title">{day['title']}</span>
            </div>
            <div class="itinerary-telemetry-badges">
              <span class="badge-telemetry">{day['alt']}</span>
              <span class="badge-telemetry">{day['time']}</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
          </button>
          <div class="itinerary-body">
            <p>{day['desc']}</p>
            {f'<div class="guide-note-box"><span class="guide-note-label">Lead Guide Field Note</span><p>{day["note"]}</p></div>' if 'note' in day else ''}
          </div>
        </div>"""

    # Build FAQ HTML
    faq_html = "".join([f"""<div class="faq-item">
      <button class="faq-trigger" onclick="const b = this.nextElementSibling; b.style.display = b.style.display === 'block' ? 'none' : 'block';">
        <span>{q}</span>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
      </button>
      <div class="faq-body" style="display: {'block' if idx == 0 else 'none'};">
        {a}
      </div>
    </div>""" for idx, (q, a) in enumerate(faqs)])

    # Full HTML Document
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | ABC Trek in Nepal</title>
  <meta name="description" content="{lead}">
  <link rel="canonical" href="https://www.abctrekinnepal.com/treks/{slug}">
  
  <link rel="stylesheet" href="../css/design-system.css">
  <link rel="stylesheet" href="../css/components.css">
</head>
<body>

  <!-- Top Announcement Bar -->
  <div class="announcement-bar">
    <div class="container announcement-inner">
      <div class="announcement-left">
        <span class="announcement-badge">{category}</span>
        <span>{title} · Pokhara & Kathmandu Operations · Licensed Mountain Guides</span>
      </div>
      <div class="announcement-right">
        <a href="https://wa.me/" class="announcement-link" style="color: #4ADE80; font-weight: 600;">
          WhatsApp Concierge: +977 980 000 0000
        </a>
      </div>
    </div>
  </div>

  <!-- Header with Mega Menu -->
  <header class="site-header">
    <div class="container">
      <div class="header-inner">
        <a href="../index" class="brand-logo">
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

        <nav class="desktop-nav">
          {get_megamenu_html("sub")}
          <div class="nav-item">
            <a href="../guide/annapurna-base-camp-trek-ultimate-guide" class="nav-link">Trek Planning</a>
          </div>
          <div class="nav-item">
            <a href="../safety-ethics/high-altitude-medical-protocols-evacuation" class="nav-link">Safety & Ethics</a>
          </div>
          <div class="nav-item">
            <a href="../company/about-us" class="nav-link">About Us</a>
          </div>
          <div class="nav-item">
            <a href="../company/contact" class="nav-link">Contact</a>
          </div>
        </nav>

        <div class="header-actions">
          <a href="../plan-your-trek" class="btn btn-primary btn-sm">Plan Your Trek</a>
          <button class="mobile-nav-toggle" id="mobileMenuOpen" aria-label="Open Navigation Menu">
            <span class="hamburger-bar"></span>
            <span class="hamburger-bar"></span>
            <span class="hamburger-bar"></span>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Mobile Navigation Drawer -->
  <div class="mobile-drawer-overlay" id="mobileOverlay" aria-hidden="true"></div>
  <div class="mobile-drawer" id="mobileMenu" role="dialog" aria-modal="true" aria-label="Mobile Navigation">
    <div class="mobile-drawer-header">
      <div class="brand-title-wrap">
        <span class="brand-name">ABC TREK</span>
        <span class="brand-tagline">IN NEPAL</span>
      </div>
      <button class="mobile-drawer-close" id="mobileMenuClose" aria-label="Close Navigation Menu">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
    </div>
    <div class="mobile-drawer-body">
      <ul class="mobile-drawer-links">
        <li><a href="../index" class="mobile-nav-link"><span>Home</span></a></li>
        <li>
          <button class="mobile-nav-link mobile-accordion-toggle" aria-expanded="false">
            <span>Annapurna Treks</span>
            <svg class="accordion-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <ul class="mobile-accordion-panel">
            <li><a href="../treks/annapurna-base-camp-classic-10-days" class="mobile-sub-link"><span>10-Day Sanctuary (Flagship)</span></a></li>
            <li><a href="../treks/8-days-annapurna-base-camp-trek" class="mobile-sub-link"><span>8 Days ABC Trek</span></a></li>
            <li><a href="../treks/short-annapurna-base-camp-trek" class="mobile-sub-link"><span>Short ABC Trek</span></a></li>
            <li><a href="../treks/annapurna-circuit-trek" class="mobile-sub-link"><span>Annapurna Circuit Trek</span></a></li>
            <li><a href="../treks/14-days-annapurna-circuit-trek" class="mobile-sub-link"><span>14 Days Circuit Trek</span></a></li>
            <li><a href="../treks/ghorepani-poon-hill-trek" class="mobile-sub-link"><span>Ghorepani Poon Hill</span></a></li>
            <li><a href="../treks/3-days-poon-hill-trek" class="mobile-sub-link"><span>3 Days Poon Hill</span></a></li>
            <li><a href="../treks/mardi-himal-trek" class="mobile-sub-link"><span>Mardi Himal Ridge</span></a></li>
            <li><a href="../treks/nar-phu-valley-trek" class="mobile-sub-link"><span>Nar Phu Valley</span></a></li>
            <li><a href="../treks/khopra-ridge-trek" class="mobile-sub-link"><span>Khopra Ridge</span></a></li>
            <li><a href="../treks/index" class="mobile-sub-link" style="font-weight: 700; color: var(--color-accent);"><span>View All 18 Treks &rarr;</span></a></li>
          </ul>
        </li>
        <li><a href="../guide/annapurna-base-camp-trek-ultimate-guide" class="mobile-nav-link"><span>Trek Planning Guide</span></a></li>
        <li><a href="../safety-ethics/high-altitude-medical-protocols-evacuation" class="mobile-nav-link"><span>Safety & Ethics</span></a></li>
        <li><a href="../company/about-us" class="mobile-nav-link"><span>About Us</span></a></li>
        <li><a href="../company/contact" class="mobile-nav-link"><span>Contact Mountain Operations</span></a></li>
      </ul>
    </div>
    <div class="mobile-drawer-footer">
      <a href="../plan-your-trek" class="btn btn-primary" style="width: 100%; text-align: center; justify-content: center;">Plan Your Trek</a>
      <a href="https://wa.me/9779818188459" class="btn btn-secondary" style="width: 100%; text-align: center; justify-content: center; color: #22C55E; border-color: #22C55E;">WhatsApp Concierge</a>
    </div>
  </div>

  <!-- Breadcrumbs -->
  <div style="background-color: var(--color-surface-subtle); border-bottom: 1px solid var(--color-border-subtle); padding: var(--space-12) 0;">
    <div class="container">
      <div class="breadcrumbs" style="margin-bottom: 0;">
        <a href="../index">Home</a>
        <span class="breadcrumb-separator">/</span>
        <a href="index">Treks</a>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">{title}</span>
      </div>
    </div>
  </div>

  <!-- Trek Hero -->
  <section class="hero-editorial" style="min-height: 55vh; padding: var(--space-48) 0;">
    <img src="{image}" alt="{title}" class="hero-background-image">
    <div class="hero-gradient-overlay"></div>
    
    <div class="container hero-content">
      <span class="eyebrow" style="color: #FDBA74;">{category} · Annapurna Region</span>
      <h1 class="hero-title" style="font-size: clamp(2.2rem, 4vw, 3.25rem);">{title}</h1>
      <p class="hero-lead">{headline}</p>

      <div class="hero-telemetry-bar">
        <div class="telemetry-item">
          <div class="telemetry-label">Duration</div>
          <div class="telemetry-value">{duration}</div>
        </div>
        <div class="telemetry-item">
          <div class="telemetry-label">Max Elevation</div>
          <div class="telemetry-value">{elevation}</div>
        </div>
        <div class="telemetry-item">
          <div class="telemetry-label">Difficulty</div>
          <div class="telemetry-value" style="font-size: 1.15rem; color: #FDBA74;">{grade}</div>
        </div>
        <div class="telemetry-item">
          <div class="telemetry-label">Starting Point</div>
          <div class="telemetry-value" style="font-size: 1.15rem;">Pokhara Hub</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Content Layout -->
  <div class="container section">
    <div class="detail-layout-grid">
      
      <!-- Left Column -->
      <main>
        <article style="margin-bottom: var(--space-48);">
          <span class="eyebrow">Expedition Architecture</span>
          <h2 style="margin-bottom: var(--space-16);">{title} – Overview</h2>
          <p class="lead">{lead}</p>
          <p>{overview}</p>

          <div class="facts-grid" style="margin-top: var(--space-24);">
            {hl_html}
          </div>
        </article>

        <!-- Itinerary Section -->
        <section style="margin-bottom: var(--space-48);">
          <div class="section-header">
            <span class="eyebrow">Field Schedule</span>
            <h2>Day-by-Day Expedition Itinerary</h2>
            <p class="section-subtitle">Paced for optimal safety, terrain enjoyment, and cultural immersion.</p>
          </div>
          <div class="itinerary-accordion">
            {itin_html}
          </div>
        </section>

        <!-- Inclusions & Exclusions -->
        <section style="margin-bottom: var(--space-48);">
          <div class="section-header">
            <span class="eyebrow">Price Integrity</span>
            <h2>Transparent Inclusions & Exclusions</h2>
          </div>
          <div class="ledger-grid">
            <div class="ledger-column inclusions">
              <div class="ledger-header">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span class="ledger-title">Included in ${price} USD</span>
              </div>
              <ul class="ledger-list">
                <li class="ledger-item">
                  <svg class="ledger-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <span><strong>All Permits:</strong> ACAP and government park entry permits.</span>
                </li>
                <li class="ledger-item">
                  <svg class="ledger-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <span><strong>Licensed Mountain Guide:</strong> English-fluent, certified in Wilderness First Aid.</span>
                </li>
                <li class="ledger-item">
                  <svg class="ledger-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <span><strong>Insured Porters (IPPG):</strong> 1 porter per 2 trekkers, 20kg maximum load cap.</span>
                </li>
                <li class="ledger-item">
                  <svg class="ledger-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <span><strong>Teahouse Lodging:</strong> Hand-vetted mountain lodges throughout the route.</span>
                </li>
                <li class="ledger-item">
                  <svg class="ledger-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <span><strong>All Meals on Trail:</strong> 3 daily meals (Breakfast, Lunch, Dinner) plus hot tea.</span>
                </li>
                <li class="ledger-item">
                  <svg class="ledger-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <span><strong>Ground Transportation:</strong> Private transport to and from trailheads.</span>
                </li>
              </ul>
            </div>

            <div class="ledger-column exclusions">
              <div class="ledger-header">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#64748B" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                <span class="ledger-title">Exclusions</span>
              </div>
              <ul class="ledger-list">
                <li class="ledger-item">
                  <svg class="ledger-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                  <span><strong>International Flights & Visa:</strong> Nepal entry tourist visa ($30/$50).</span>
                </li>
                <li class="ledger-item">
                  <svg class="ledger-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                  <span><strong>Emergency Travel Insurance:</strong> Mandatory policy covering high altitude and rescue.</span>
                </li>
                <li class="ledger-item">
                  <svg class="ledger-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                  <span><strong>Teahouse Incidentals:</strong> Hot showers, Wi-Fi cards, and device charging fees.</span>
                </li>
                <li class="ledger-item">
                  <svg class="ledger-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                  <span><strong>Personal Gear & Tipping:</strong> Discretionary gratuity for guide and porters.</span>
                </li>
              </ul>
            </div>
          </div>
        </section>

        <!-- FAQs -->
        <section style="margin-bottom: var(--space-48);">
          <div class="section-header">
            <span class="eyebrow">Practical Intelligence</span>
            <h2>Frequently Answered Questions</h2>
          </div>
          <div class="faq-accordion">
            {faq_html}
          </div>
        </section>
      </main>

      <!-- Right Column: Booking Card -->
      <aside>
        <div class="booking-card">
          <div class="booking-price-row">
            <span class="price-subtext">Expedition Package Price</span>
            <div class="price-main">${price} <span>USD / Person</span></div>
            <div style="font-size: var(--text-caption); color: var(--color-success); font-weight: 600; margin-top: 4px;">
              ✓ All Permits, Lodging, Meals & Transport Included
            </div>
          </div>

          <div style="margin-bottom: var(--space-20);">
            <div style="display: flex; justify-content: space-between; font-size: var(--text-body-sm); margin-bottom: 8px;">
              <span style="color: var(--color-text-muted);">Duration:</span>
              <strong>{duration}</strong>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: var(--text-body-sm); margin-bottom: 8px;">
              <span style="color: var(--color-text-muted);">Max Altitude:</span>
              <strong>{elevation}</strong>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: var(--text-body-sm); margin-bottom: 8px;">
              <span style="color: var(--color-text-muted);">Group Size:</span>
              <strong>Max 8 Trekkers</strong>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: var(--text-body-sm);">
              <span style="color: var(--color-text-muted);">Season:</span>
              <strong>Autumn & Spring 2026</strong>
            </div>
          </div>

          <div style="display: flex; flex-direction: column; gap: var(--space-12);">
            <a href="../plan-your-trek" class="btn btn-primary btn-lg" style="width: 100%;">
              Inquire / Check Dates
            </a>
            <a href="https://wa.me/" class="btn btn-whatsapp" style="width: 100%;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.664-.699c.97.54 1.769.818 2.802.818 3.18 0 5.767-2.587 5.767-5.766.001-3.182-2.585-5.77-5.773-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.698.073-.977-.014-.235-.074-.537-.179-1.04-.395-2.146-.92-3.535-3.097-3.642-3.239-.107-.142-.871-1.16-.871-2.213s.553-1.572.749-1.787c.196-.215.428-.269.571-.269s.286.005.41.011c.13.007.306-.05.479.366.179.431.609 1.488.662 1.595.053.107.089.233.018.376-.071.143-.107.233-.214.358-.107.125-.227.28-.324.376-.107.107-.219.223-.094.438.125.215.556.915 1.192 1.482.818.729 1.509.954 1.723 1.061.214.107.34.089.465-.054.125-.143.536-.626.679-.841.143-.215.286-.179.482-.107s1.25.59 1.464.697c.214.107.357.161.41.25.054.089.054.519-.089.924z"/></svg>
              Chat on WhatsApp
            </a>
          </div>

          <div class="booking-guarantee-strip">
            <div class="guarantee-item">
              <svg class="guarantee-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
              <span>Free date rescheduling up to 30 days prior</span>
            </div>
            <div class="guarantee-item">
              <svg class="guarantee-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
              <span>100% Licensed Himalayan Mountain Guides</span>
            </div>
            <div class="guarantee-item">
              <svg class="guarantee-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
              <span>IPPG Ethical Porter Standards (20kg load cap)</span>
            </div>
          </div>
        </div>
      </aside>
    </div>
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
            <li><a href="annapurna-base-camp-classic-10-days" class="footer-link">10-Day Classic Sanctuary (Flagship)</a></li>
            <li><a href="annapurna-circuit-trek" class="footer-link">Annapurna Circuit Trek</a></li>
            <li><a href="ghorepani-poon-hill-trek" class="footer-link">Ghorepani Poon Hill Trek</a></li>
            <li><a href="mardi-himal-trek" class="footer-link">Mardi Himal Trek</a></li>
            <li><a href="index" class="footer-link">All Annapurna Routes</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-col-title">Trekker Resources</div>
          <ul class="footer-links">
            <li><a href="../guide/annapurna-base-camp-trek-ultimate-guide" class="footer-link">Ultimate ABC Guide (2026)</a></li>
            <li><a href="../safety-ethics/high-altitude-medical-protocols-evacuation" class="footer-link">Altitude Sickness Science</a></li>
            <li><a href="../guide/annapurna-base-camp-trek-ultimate-guide#packing" class="footer-link">Complete Packing Checklist</a></li>
            <li><a href="../guide/annapurna-base-camp-trek-ultimate-guide#permits" class="footer-link">2026 ACAP Permits & Rules</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-col-title">Trust & Support</div>
          <ul class="footer-links">
            <li><a href="../safety-ethics/high-altitude-medical-protocols-evacuation" class="footer-link">Medical Protocols & Rescue</a></li>
            <li><a href="../company/about-us" class="footer-link">About Our Mountain Team</a></li>
            <li><a href="../company/contact" class="footer-link">Contact Operations Base</a></li>
            <li><a href="../plan-your-trek" class="footer-link">Interactive Trip Builder</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 ABC Trek in Nepal. All rights reserved.</div>
        <div style="display: flex; gap: var(--space-16);">
          <a href="../company/about-us" class="footer-link">Privacy Policy</a>
          <a href="../company/about-us" class="footer-link">Terms & Conditions</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Mobile Sticky Conversion Bar -->
  <div class="mobile-sticky-bar">
    <div class="mobile-sticky-inner">
      <div class="sticky-price-block">
        <span class="sticky-price-label">{title}</span>
        <span class="sticky-price-val">${price} <span>USD</span></span>
      </div>
      <div style="display: flex; gap: var(--space-8);">
        <a href="../plan-your-trek" class="btn btn-primary btn-sm">Inquire</a>
        <a href="https://wa.me/" class="btn btn-whatsapp btn-sm" aria-label="WhatsApp">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.664-.699c.97.54 1.769.818 2.802.818 3.18 0 5.767-2.587 5.767-5.766.001-3.182-2.585-5.77-5.773-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.698.073-.977-.014-.235-.074-.537-.179-1.04-.395-2.146-.92-3.535-3.097-3.642-3.239-.107-.142-.871-1.16-.871-2.213s.553-1.572.749-1.787c.196-.215.428-.269.571-.269s.286.005.41.011c.13.007.306-.05.479.366.179.431.609 1.488.662 1.595.053.107.089.233.018.376-.071.143-.107.233-.214.358-.107.125-.227.28-.324.376-.107.107-.219.223-.094.438.125.215.556.915 1.192 1.482.818.729 1.509.954 1.723 1.061.214.107.34.089.465-.054.125-.143.536-.626.679-.841.143-.215.286-.179.482-.107s1.25.59 1.464.697c.214.107.357.161.41.25.054.089.054.519-.089.924z"/></svg>
        </a>
      </div>
    </div>
  </div>

  <script src="../js/nav.js" defer></script>
</body>
</html>"""
    return html

print("Generator template ready.")
