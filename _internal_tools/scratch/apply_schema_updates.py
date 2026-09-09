import re
import json

def update_september_guide():
    path = 'guide/annapurna-base-camp-trek-september.html'
    content = open(path, encoding='utf-8').read()
    
    # Target the end of FAQPage block inside the @graph array
    old_end = '''              "text": "It's rare. Temperatures at base camp in September generally stay just above the point of consistent snowfall, though a light sleet or brief dusting is possible above 3,500 m during a late-month cold snap. Real, consistent snow cover doesn't typically arrive until late November onward."
            }
          }
        ]
      }
    ]
  }
  </script>'''

    new_end = '''              "text": "It's rare. Temperatures at base camp in September generally stay just above the point of consistent snowfall, though a light sleet or brief dusting is possible above 3,500 m during a late-month cold snap. Real, consistent snow cover doesn't typically arrive until late November onward."
            }
          }
        ]
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://www.abctrekinnepal.com/"
          },
          {
            "@type": "ListItem",
            "position": 2,
            "name": "Guides",
            "item": "https://www.abctrekinnepal.com/guide/annapurna-base-camp-trek"
          },
          {
            "@type": "ListItem",
            "position": 3,
            "name": "ABC Trek in September",
            "item": "https://www.abctrekinnepal.com/guide/annapurna-base-camp-trek-september"
          }
        ]
      }
    ]
  }
  </script>'''

    assert old_end in content, 'Target in September guide not found'
    content = content.replace(old_end, new_end)
    
    # Verify valid JSON
    m = re.search(r'<script\s+type=[\'"]application/ld\+json[\'"]>([\s\S]*?)</script>', content)
    json.loads(m.group(1))
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated guide/annapurna-base-camp-trek-september.html with BreadcrumbList')

def update_pillar_guide():
    path = 'guide/annapurna-base-camp-trek.html'
    content = open(path, encoding='utf-8').read()
    
    old_schema = '''  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "The Ultimate Guide to Annapurna Base Camp Trek (2026 Edition)",
    "description": "The definitive field planning guide for Annapurna Base Camp trek. Route itineraries, month-by-month weather, packing checklist, altitude safety, permits, and teahouse realities.",
    "author": {
      "@type": "Person",
      "name": "Sugam Shrestha",
      "jobTitle": "Founder, Expedition Director & Lead Mountain Specialist",
      "url": "https://www.abctrekinnepal.com/company/about-us",
      "worksFor": {
        "@type": "TravelAgency",
        "name": "ABC Trek in Nepal",
        "telephone": "+977-9818188459",
        "address": "Budhanilkantha, Kathmandu, Nepal"
      }
    },
    "publisher": {
      "@type": "Organization",
      "name": "ABC Trek in Nepal",
      "url": "https://www.abctrekinnepal.com/"
    },
    "datePublished": "2026-01-15",
    "dateModified": "2026-09-01"
  }
  </script>'''

    new_schema = '''  <!-- Structured Data (JSON-LD): Article & BreadcrumbList -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Article",
        "@id": "https://www.abctrekinnepal.com/guide/annapurna-base-camp-trek#article",
        "headline": "The Ultimate Guide to Annapurna Base Camp Trek (2026 Edition)",
        "description": "The definitive field planning guide for Annapurna Base Camp trek. Route itineraries, month-by-month weather, packing checklist, altitude safety, permits, and teahouse realities.",
        "image": "https://www.abctrekinnepal.com/images/logo.png",
        "datePublished": "2026-01-15",
        "dateModified": "2026-09-09",
        "mainEntityOfPage": "https://www.abctrekinnepal.com/guide/annapurna-base-camp-trek",
        "author": {
          "@type": "Person",
          "name": "Sugam Shrestha",
          "jobTitle": "Founder, Expedition Director & Lead Mountain Specialist",
          "url": "https://www.abctrekinnepal.com/team/sugam-shrestha",
          "worksFor": {
            "@type": "TravelAgency",
            "name": "ABC Trek in Nepal",
            "telephone": "+977-9818188459",
            "address": "Budhanilkantha, Kathmandu, Nepal"
          }
        },
        "publisher": {
          "@type": "Organization",
          "name": "ABC Trek in Nepal",
          "url": "https://www.abctrekinnepal.com/",
          "logo": {
            "@type": "ImageObject",
            "url": "https://www.abctrekinnepal.com/images/logo.png"
          }
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://www.abctrekinnepal.com/"
          },
          {
            "@type": "ListItem",
            "position": 2,
            "name": "Guides",
            "item": "https://www.abctrekinnepal.com/treks"
          },
          {
            "@type": "ListItem",
            "position": 3,
            "name": "Ultimate ABC Guide (2026)",
            "item": "https://www.abctrekinnepal.com/guide/annapurna-base-camp-trek"
          }
        ]
      }
    ]
  }
  </script>'''

    assert old_schema in content, 'Old schema in pillar guide not found'
    content = content.replace(old_schema, new_schema)
    
    m = re.search(r'<script\s+type=[\'"]application/ld\+json[\'"]>([\s\S]*?)</script>', content)
    json.loads(m.group(1))
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated guide/annapurna-base-camp-trek.html with Article & Breadcrumbs')

def update_safety_page():
    path = 'safety-ethics/high-altitude-medical-protocols-evacuation.html'
    content = open(path, encoding='utf-8').read()
    
    target_pos = content.find('</head>')
    assert target_pos != -1, '</head> not found in safety page'
    
    safety_schema = '''  <!-- Structured Data (JSON-LD): Article & BreadcrumbList -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Article",
        "@id": "https://www.abctrekinnepal.com/safety-ethics/high-altitude-medical-protocols-evacuation#article",
        "headline": "High-Altitude Medical Protocols & Porter Welfare in the Annapurna Sanctuary",
        "description": "Clinical altitude protocols, daily pulse oximetry checks, emergency helicopter evacuation procedures, and IPPG ethical porter welfare standards in the Annapurna Sanctuary.",
        "image": "https://www.abctrekinnepal.com/images/logo.png",
        "datePublished": "2026-02-01",
        "dateModified": "2026-09-09",
        "mainEntityOfPage": "https://www.abctrekinnepal.com/safety-ethics/high-altitude-medical-protocols-evacuation",
        "author": {
          "@type": "Person",
          "name": "Sugam Shrestha",
          "jobTitle": "Founder, Expedition Director & Lead Mountain Specialist",
          "url": "https://www.abctrekinnepal.com/team/sugam-shrestha",
          "knowsAbout": [
            "Wilderness First Responder (WFR)",
            "High Altitude Mountain Acclimatization",
            "Emergency Helicopter Evacuation",
            "IPPG Porter Welfare Charter"
          ],
          "worksFor": {
            "@type": "TravelAgency",
            "name": "ABC Trek in Nepal",
            "telephone": "+977-9818188459",
            "address": "Budhanilkantha, Kathmandu, Nepal"
          }
        },
        "publisher": {
          "@type": "Organization",
          "name": "ABC Trek in Nepal",
          "url": "https://www.abctrekinnepal.com/",
          "logo": {
            "@type": "ImageObject",
            "url": "https://www.abctrekinnepal.com/images/logo.png"
          }
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://www.abctrekinnepal.com/"
          },
          {
            "@type": "ListItem",
            "position": 2,
            "name": "Safety & Ethics",
            "item": "https://www.abctrekinnepal.com/safety-ethics/high-altitude-medical-protocols-evacuation"
          }
        ]
      }
    ]
  }
  </script>
'''
    content = content[:target_pos] + safety_schema + content[target_pos:]
    
    m = re.search(r'<script\s+type=[\'"]application/ld\+json[\'"]>([\s\S]*?)</script>', content)
    json.loads(m.group(1))
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated safety-ethics page with Article & Breadcrumbs schema')

def update_10day_classic():
    path = 'treks/annapurna-base-camp-classic-10-days.html'
    content = open(path, encoding='utf-8').read()
    
    target_pos = content.find('</head>')
    assert target_pos != -1, '</head> not found in 10-day trek'
    
    trek_schema = '''  <!-- Structured Data (JSON-LD): TouristTrip & BreadcrumbList -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "TouristTrip",
        "@id": "https://www.abctrekinnepal.com/treks/annapurna-base-camp-classic-10-days#trip",
        "name": "Annapurna Base Camp Trek – The Classic 10-Day Sanctuary Expedition",
        "description": "The gold-standard 10-day Annapurna Base Camp trek from Pokhara. Conservative acclimatization pacing, curated teahouse lodging, licensed local mountain leaders, and full ACAP permits.",
        "touristType": "Hikers & Trekkers",
        "offers": {
          "@type": "Offer",
          "price": "890",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock",
          "validFrom": "2026-01-01",
          "url": "https://www.abctrekinnepal.com/treks/annapurna-base-camp-classic-10-days"
        },
        "provider": {
          "@type": "TravelAgency",
          "name": "ABC Trek in Nepal",
          "url": "https://www.abctrekinnepal.com/",
          "telephone": "+977-9818188459",
          "address": "Budhanilkantha, Kathmandu, Nepal"
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://www.abctrekinnepal.com/"
          },
          {
            "@type": "ListItem",
            "position": 2,
            "name": "Annapurna Treks",
            "item": "https://www.abctrekinnepal.com/treks"
          },
          {
            "@type": "ListItem",
            "position": 3,
            "name": "10-Day Classic Sanctuary",
            "item": "https://www.abctrekinnepal.com/treks/annapurna-base-camp-classic-10-days"
          }
        ]
      }
    ]
  }
  </script>
'''
    content = content[:target_pos] + trek_schema + content[target_pos:]
    
    m = re.search(r'<script\s+type=[\'"]application/ld\+json[\'"]>([\s\S]*?)</script>', content)
    json.loads(m.group(1))
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated 10-day classic trek page with TouristTrip & Breadcrumbs schema')

if __name__ == '__main__':
    update_september_guide()
    update_pillar_guide()
    update_safety_page()
    update_10day_classic()
    print('ALL SCHEMAS APPLIED AND SYNTACTICALLY VALIDATED!')
