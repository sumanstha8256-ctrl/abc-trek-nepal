import re

def main():
    path = 'guide/annapurna-base-camp-trek-september.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Author byline link
    old_byline = '<span><strong>Author:</strong> Sugam Shrestha (Expedition Director)</span>\n            <span>•</span>\n            <span><strong>Reading Time:</strong> 15 Minutes</span>\n            <span>•</span>\n            <span><strong>Field Verification:</strong> 2026 ACAP Protocols</span>'
    new_byline = '<span><strong>Author:</strong> <a href="/team/sugam-shrestha" style="color: inherit; text-decoration: underline;">Sugam Shrestha (Expedition Director)</a></span>\n            <span>•</span>\n            <span><strong>Reading Time:</strong> 15 Minutes</span>\n            <span>•</span>\n            <span><strong>Field Verification:</strong> <a href="/company/about-us" style="color: inherit; text-decoration: underline;">Mountain Operations Base</a></span>'

    assert old_byline in content, 'Byline not found'
    content = content.replace(old_byline, new_byline)

    # 2. Intro lead paragraphs
    old_intro = '''          <p class="lead" style="margin-bottom: var(--space-20); font-size: var(--text-body-lg); color: var(--color-text-muted); line-height: 1.7;">
            The Annapurna Base Camp Trek takes you from the hills around Pokhara through mountain villages and the Annapurna Sanctuary to Annapurna Base Camp at 4,130 m (13,550 ft), with views of peaks such as Annapurna I (8,091 m) and Machhapuchhre. The trek typically takes 7–12 days, with overnight stays in teahouses.
          </p>
          <p style="font-size: var(--text-body-md); color: var(--color-text-body); line-height: 1.75; margin-bottom: var(--space-20);">
            September can be a good month for the Annapurna Base Camp Trek, but conditions vary throughout the month. Early September can still be rainy, muddy, and cloudy as the monsoon ends, while the weather generally becomes drier and clearer toward late September. If your dates are flexible, late September is usually the better choice.
          </p>
          <p style="font-size: var(--text-body-md); color: var(--color-text-body); line-height: 1.75; margin-bottom: var(--space-24);">
            This guide covers September weather and temperature, rainfall, trail conditions, mountain views, itinerary, difficulty, cost, permits, accommodation, packing, transportation, altitude safety, and how September compares with October and November.
          </p>'''

    new_intro = '''          <p class="lead" style="margin-bottom: var(--space-20); font-size: var(--text-body-lg); color: var(--color-text-muted); line-height: 1.7;">
            The <a href="/treks/annapurna-base-camp-classic-10-days" style="color: var(--color-brand-dark); font-weight: 700; text-decoration: underline;">Annapurna Base Camp Trek</a> takes you from the foothills around Pokhara through mountain villages and the Annapurna Sanctuary to Annapurna Base Camp at 4,130 m (13,550 ft), surrounded by peaks like Annapurna I (8,091 m) and Machhapuchhre (6,993 m). The trek typically takes 7–12 days, with overnight stays in high-altitude teahouses.
          </p>
          <p style="font-size: var(--text-body-md); color: var(--color-text-body); line-height: 1.75; margin-bottom: var(--space-20);">
            September can be a rewarding month for trekking to Annapurna Base Camp, but conditions vary substantially across its 30 days. Early September still brings tail-monsoon showers and muddy trails, while late September ushers in clear skies and crisp Himalayan panoramas. For comprehensive seasonal breakdowns, see our <a href="/guide/annapurna-base-camp-trek" style="color: var(--color-accent); font-weight: 600;">Complete Annapurna Base Camp Trek Planning Guide</a>.
          </p>
          <p style="font-size: var(--text-body-md); color: var(--color-text-body); line-height: 1.75; margin-bottom: var(--space-24);">
            This authoritative field guide covers September weather, temperature gradients, trail conditions, duration variants from our <a href="/treks/short-annapurna-base-camp-trek" style="color: var(--color-brand-dark); text-decoration: underline;">Short ABC Trek</a> to the <a href="/treks/annapurna-base-camp-classic-10-days" style="color: var(--color-brand-dark); text-decoration: underline;">10-Day Classic Sanctuary</a>, permit logistics, packing essentials, and altitude safety protocols.
          </p>'''

    assert old_intro in content, 'Intro not found'
    content = content.replace(old_intro, new_intro)

    # 3. Is September a good month
    old_good = '''          <p>
            September sits at the monsoon-to-autumn transition, which brings three things together: the greenest scenery of the year, the fullest waterfalls, and fewer trekkers than October or November. The trade-off is less predictable weather than in October.
          </p>'''

    new_good = '''          <p>
            September sits at the monsoon-to-autumn transition, which brings three unique advantages: the greenest alpine scenery of the year, cascading full-flow waterfalls, and significantly fewer trekkers than peak October or November. For trekkers wanting tranquility, our <a href="/treks/annapurna-base-camp-classic-10-days" style="color: var(--color-accent); font-weight: 600;">10-Day Classic Sanctuary Trek</a> in late September offers an ideal balance of calm trails and emerging crystal clarity.
          </p>'''

    assert old_good in content, 'Good section not found'
    content = content.replace(old_good, new_good)

    # 4. Trail conditions - guide knowledge
    old_trail = '''            <li><strong>Landslide risk:</strong> Highest June–August; still elevated in early September on steep, exposed sections after heavy rain, then drops off. A guide's current knowledge of trail conditions matters more here than in the dry months.</li>'''

    new_trail = '''            <li><strong>Landslide risk:</strong> Highest June–August; still elevated in early September on steep, exposed sections after heavy rain, then drops off. A guide's current knowledge of trail conditions matters more here than in dry months — our lead specialist <a href="/team/sugam-shrestha" style="color: var(--color-brand-dark); font-weight: 600; text-decoration: underline;">Sugam Shrestha</a> and field guides continuously assess Modi Khola gorge stability daily.</li>'''

    assert old_trail in content, 'Trail section not found'
    content = content.replace(old_trail, new_trail)

    # 5. Route and Elevation
    old_route = '''          <p>
            The trek climbs from the Modi Khola trailheads — Nayapul (1,070 m) or modern jeep heads like Kimche, Matque, and Siwai (1,200–1,500 m) — up to Annapurna Base Camp (4,130 m), a net gain of over 3,000 m through forest, farmland, and mountain villages. The route doesn't change by season — only ground conditions do.
          </p>
          <p>
            <strong>Start / End:</strong> Nayapul, or one of the newer jeep trailheads (Kimche, Matque, Siwai) for a shorter walk-in, to Pokhara, exiting via Jhinu Danda's hot springs.
          </p>
          <p>
            <strong>Route sequence:</strong> Nayapul &rarr; Ghandruk / Tikhedhunga &rarr; Ghorepani &rarr; Poon Hill &rarr; Tadapani &rarr; Chhomrong &rarr; Sinuwa &rarr; Bamboo &rarr; Dovan &rarr; Himalaya &rarr; Deurali &rarr; Machhapuchhre Base Camp &rarr; Annapurna Base Camp, then back down via Jhinu Danda to Pokhara. It's a there-and-back walk through the Modi Khola valley, not a loop.
          </p>'''

    new_route = '''          <p>
            The trek climbs from the Modi Khola trailheads — Nayapul (1,070 m) or modern jeep heads like Kimche, Matque, and Siwai (1,200–1,500 m) — up to Annapurna Base Camp (4,130 m), a net gain of over 3,000 m through forest, farmland, and mountain villages. The classic route is detailed in our <a href="/treks/annapurna-base-camp-classic-10-days" style="color: var(--color-accent); font-weight: 600;">10-Day Annapurna Base Camp Classic Package</a>, while time-conscious hikers can opt for the <a href="/treks/short-annapurna-base-camp-trek" style="color: var(--color-accent); font-weight: 600;">Short ABC Trek</a> or <a href="/treks/8-days-annapurna-base-camp-trek" style="color: var(--color-accent); font-weight: 600;">8-Day Rapid ABC Route</a>.
          </p>
          <p>
            <strong>Start / End:</strong> Nayapul or upper jeep trailheads to Pokhara, concluding with a therapeutic soak in Jhinu Danda's natural riverside hot springs.
          </p>
          <p>
            <strong>Route sequence:</strong> Nayapul &rarr; Tikhedhunga &rarr; Ghorepani &rarr; Poon Hill &rarr; Tadapani &rarr; Chhomrong &rarr; Sinuwa &rarr; Bamboo &rarr; Dovan &rarr; Himalaya &rarr; Deurali &rarr; Machhapuchhre Base Camp &rarr; Annapurna Base Camp, then down via Jhinu Danda to Pokhara. Those wishing to add sunrise panoramas can explore our <a href="/treks/ghorepani-poon-hill-trek" style="color: var(--color-brand-dark); text-decoration: underline;">Ghorepani Poon Hill Trek</a>, or consider the ridge scenery of the <a href="/treks/mardi-himal-trek" style="color: var(--color-brand-dark); text-decoration: underline;">Mardi Himal Trek</a>.
          </p>'''

    assert old_route in content, 'Route section not found'
    content = content.replace(old_route, new_route)

    # 6. Duration table links
    old_dur_table = '''                <tr>
                  <td><strong>7-day (via Ghandruk, no Poon Hill)</strong></td>
                  <td>7</td>
                  <td>Short on time</td>
                </tr>
                <tr>
                  <td><strong>8-day (with Poon Hill)</strong></td>
                  <td>8</td>
                  <td>Compact but wants the viewpoint</td>
                </tr>
                <tr>
                  <td><strong>10-day (standard pace)</strong></td>
                  <td>10</td>
                  <td>First-timers; anyone trekking early September</td>
                </tr>'''

    new_dur_table = '''                <tr>
                  <td><strong><a href="/treks/short-annapurna-base-camp-trek" style="color: var(--color-brand-dark); text-decoration: underline;">7-Day Express (via Ghandruk, no Poon Hill)</a></strong></td>
                  <td>7</td>
                  <td>Short on time; strong fitness required</td>
                </tr>
                <tr>
                  <td><strong><a href="/treks/8-days-annapurna-base-camp-trek" style="color: var(--color-brand-dark); text-decoration: underline;">8-Day Rapid (with Poon Hill)</a></strong></td>
                  <td>8</td>
                  <td>Compact schedule with Poon Hill sunrise</td>
                </tr>
                <tr>
                  <td><strong><a href="/treks/annapurna-base-camp-classic-10-days" style="color: var(--color-brand-dark); text-decoration: underline;">10-Day Classic Sanctuary (Recommended)</a></strong></td>
                  <td>10</td>
                  <td>Optimal acclimatization, buffer days & first-timers</td>
                </tr>'''

    assert old_dur_table in content, 'Duration table not found'
    content = content.replace(old_dur_table, new_dur_table)

    # 6b. Buffer day paragraph
    old_buffer = '''          <p>
            <strong>Buffer day:</strong> Worth adding if trekking in the first half of September, to absorb a rain delay or a clouded-over Poon Hill sunrise without losing your summit day. Less essential once the weather has settled late-month.
          </p>'''

    new_buffer = '''          <p>
            <strong>Buffer day:</strong> Highly recommended if trekking in early September to absorb weather delays without compromising base camp arrival. You can build customized contingency days using our interactive <a href="/plan-your-trek" style="color: var(--color-accent); font-weight: 700;">Trip Planning Wizard &rarr;</a>
          </p>'''

    assert old_buffer in content, 'Buffer section not found'
    content = content.replace(old_buffer, new_buffer)

    # 7. Itinerary section intro
    old_itin_intro = '''          <h2 style="margin-bottom: var(--space-16);">Itinerary in September</h2>
          <p>
            Same route every month; the reasoning behind pacing matters more in September, since ground conditions shift as the month goes on.
          </p>'''

    new_itin_intro = '''          <h2 style="margin-bottom: var(--space-16);">Itinerary in September</h2>
          <p>
            The physical route follows our benchmark <a href="/treks/annapurna-base-camp-classic-10-days" style="color: var(--color-accent); font-weight: 600;">10-Day Annapurna Base Camp Classic Itinerary</a>. In September, deliberate pacing allows your team to navigate morning cloud patterns and avoid afternoon showers:
          </p>'''

    assert old_itin_intro in content, 'Itin intro not found'
    content = content.replace(old_itin_intro, new_itin_intro)

    # 7b. Itinerary post-stepper
    old_itin_post = '''          <p>
            <strong>Why duration varies:</strong> Whether Poon Hill is included, how many buffer days you add, and where you start walking from (Nayapul vs. driving further in to Kimche/Matque).
          </p>
          <p>
            <strong>Keep flexibility in your schedule:</strong> A day or two of slack lets you wait out bad weather instead of pushing through low visibility just to stay on plan. This matters more in September than in almost any other month.
          </p>'''

    new_itin_post = '''          <p>
            <strong>Why duration varies:</strong> Whether Poon Hill is included via the <a href="/treks/ghorepani-poon-hill-trek" style="color: var(--color-brand-dark); text-decoration: underline;">Poon Hill circuit</a>, how many buffer days you add, and where you start walking from.
          </p>
          <p>
            <strong>Keep flexibility in your schedule:</strong> A day or two of slack lets you wait out bad weather instead of pushing through low visibility. Build your bespoke itinerary with our <a href="/plan-your-trek" style="color: var(--color-accent); font-weight: 700;">Interactive Trek Planner &rarr;</a>
          </p>'''

    assert old_itin_post in content, 'Itin post not found'
    content = content.replace(old_itin_post, new_itin_post)

    # 8. Cost section
    old_cost = '''          <p>
            <strong>What's included in our packages:</strong> All required ACAP permits, licensed mountain leader guide, porter logistics, high-altitude teahouse accommodation, private ground transport, and comprehensive safety monitoring.
          </p>'''

    new_cost = '''          <p>
            <strong>What's included in our packages:</strong> All required ACAP permits, licensed mountain leaders, porter logistics, teahouses, private transport, and safety monitoring — view complete inclusions on our <a href="/treks/annapurna-base-camp-classic-10-days" style="color: var(--color-accent); font-weight: 600;">10-Day Classic Sanctuary page</a>.
          </p>'''

    assert old_cost in content, 'Cost section not found'
    content = content.replace(old_cost, new_cost)

    # 9. Guide or Porter?
    old_gp = '''          <p>
            A guide leads the trek, knows current trail conditions (valuable for spotting mud or unstable sections early in the month), and handles safety and language. A porter carries baggage — typically up to 15–20 kg between two trekkers — reducing physical strain, especially useful when the trail is heavier going. Costs for both are usually bundled into a package price. For first-time trekkers, both together (guide required, porter optional) is the easiest combination.
          </p>'''

    new_gp = '''          <p>
            A licensed guide leads the trek, monitors trail conditions in real-time, and administers wilderness first aid. Led by <a href="/team/sugam-shrestha" style="color: var(--color-brand-dark); font-weight: 600; text-decoration: underline;">Sugam Shrestha</a>, all our mountain leaders are certified in high-altitude medicine and emergency evacuation. A porter carries heavy duffels (strictly capped at 20 kg between two trekkers under our <a href="/company/about-us" style="color: var(--color-brand-dark); font-weight: 600; text-decoration: underline;">ethical porter welfare standards</a>), easing physical strain so you can focus on foot placement on wet stone staircases.
          </p>'''

    assert old_gp in content, 'Guide/porter section not found'
    content = content.replace(old_gp, new_gp)

    # 10. Permits & Contacts
    old_permits = '''          <p>
            A licensed guide has been mandatory since April 2023 — independent solo trekking is no longer permitted. Trekking without a valid permit can mean fines or being turned back. Fees and rules change — confirm with a registered agency close to your travel date.
          </p>'''

    new_permits = '''          <p>
            A licensed guide has been mandatory since April 2023 — independent solo trekking is no longer permitted. Checkpoints in Birethanti and Chhomrong strictly inspect both ACAP paperwork and your guide's government credentials. Our team manages all administrative clearances directly through our <a href="/company/contact" style="color: var(--color-accent); font-weight: 600;">Kathmandu &amp; Pokhara operations bases</a>.
          </p>'''

    assert old_permits in content, 'Permits section not found'
    content = content.replace(old_permits, new_permits)

    # 11. September vs Other Months
    old_comp = '''          <p>
            <strong>vs. October/November:</strong> Less weather certainty, but greener scenery and far fewer people.
          </p>
          <p>
            <strong>vs. August:</strong> A clear step up — August is still full monsoon with high leeches, closed trailheads, and continuous deluge.
          </p>
          <p>
            <strong>vs. April:</strong> Different look (post-monsoon green vs. spring rhododendron bloom), similar dryness by late September, but April carries October-level crowds.
          </p>'''

    new_comp = '''          <p>
            <strong>vs. October/November:</strong> Less weather certainty, but vibrant emerald scenery and far fewer people. For details on peak autumn months, see our <a href="/guide/annapurna-base-camp-trek" style="color: var(--color-accent); font-weight: 600;">Ultimate Guide to Annapurna Base Camp</a>.
          </p>
          <p>
            <strong>vs. August:</strong> A clear step up — August is full monsoon with pervasive leeches, river surges, and persistent cloud cover.
          </p>
          <p>
            <strong>vs. High Pass Treks:</strong> If you seek alpine passes rather than a valley sanctuary, late September is also the prime opening window for the <a href="/treks/14-days-annapurna-circuit-trek" style="color: var(--color-accent); font-weight: 600;">14-Day Annapurna Circuit Trek</a> over Thorong La (5,416 m).
          </p>'''

    assert old_comp in content, 'Comp section not found'
    content = content.replace(old_comp, new_comp)

    # 12. Author Box
    old_author = '''              <div style="font-weight: 700; color: var(--color-brand-dark); font-size: 1.15rem;">Field Intelligence by Sugam Shrestha</div>'''
    new_author = '''              <div style="font-weight: 700; color: var(--color-brand-dark); font-size: 1.15rem;"><a href="/team/sugam-shrestha" style="color: var(--color-brand-dark); text-decoration: underline;">Field Intelligence by Sugam Shrestha</a></div>'''

    assert old_author in content, 'Author box not found'
    content = content.replace(old_author, new_author)

    old_author_desc = 'Sugam oversees expedition logistics and conservative acclimatization protocols through the Modi Khola gorge into the Sanctuary.'
    new_author_desc = 'Sugam oversees expedition logistics and conservative acclimatization protocols through the Modi Khola gorge into the Sanctuary. View his certifications and leadership record on his <a href="/team/sugam-shrestha" style="color: var(--color-accent); font-weight: 600;">Expedition Director Profile &rarr;</a>'

    assert old_author_desc in content, 'Author desc not found'
    content = content.replace(old_author_desc, new_author_desc)

    # 13. Related Guides & Expeditions Grid (insert before Conclusion)
    old_conc = '        <!-- Section: Conclusion -->'
    new_related_and_conc = '''        <!-- Related Annapurna Field Guides & Packages Hub -->
        <section class="related-resources-hub" style="margin-bottom: var(--space-48);">
          <div class="section-header" style="margin-bottom: var(--space-24);">
            <span class="eyebrow">Related Annapurna Field Intelligence</span>
            <h2 style="font-size: 1.5rem; margin-bottom: 8px;">Explore Companion Guides &amp; Route Packages</h2>
            <p style="color: var(--color-text-muted); margin-bottom: 0;">
              Continue preparing for your Himalaya journey with our verified trekker dossiers and routes:
            </p>
          </div>

          <div class="blog-cards-grid">
            <div class="blog-card">
              <div class="blog-card-content">
                <span class="eyebrow">Flagship Route</span>
                <h3 class="blog-card-title">
                  <a href="/treks/annapurna-base-camp-classic-10-days">10-Day ABC Classic Sanctuary</a>
                </h3>
                <p class="blog-card-excerpt">
                  The gold-standard itinerary into the 4,130m amphitheater with conservative acclimatization, licensed Sherpa leaders, and teahouse bookings.
                </p>
                <a href="/treks/annapurna-base-camp-classic-10-days" class="nav-link" style="color: var(--color-accent); font-weight: 700; margin-top: auto;">Explore Itinerary &rarr;</a>
              </div>
            </div>

            <div class="blog-card">
              <div class="blog-card-content">
                <span class="eyebrow">Pillar Field Guide</span>
                <h3 class="blog-card-title">
                  <a href="/guide/annapurna-base-camp-trek">The Complete ABC Guide (2026)</a>
                </h3>
                <p class="blog-card-excerpt">
                  The encyclopedic master guide covering packing essentials, permits, season-by-season conditions, teahouse realities, and safety rules.
                </p>
                <a href="/guide/annapurna-base-camp-trek" class="nav-link" style="color: var(--color-accent); font-weight: 700; margin-top: auto;">Read Master Guide &rarr;</a>
              </div>
            </div>

            <div class="blog-card">
              <div class="blog-card-content">
                <span class="eyebrow">Safety & Protocols</span>
                <h3 class="blog-card-title">
                  <a href="/safety-ethics/high-altitude-medical-protocols-evacuation">Altitude Safety &amp; Heli Evacuation</a>
                </h3>
                <p class="blog-card-excerpt">
                  Wilderness medicine protocols, AMS symptoms management, pulse oximetry thresholds, and emergency helicopter rescue procedures in the Sanctuary.
                </p>
                <a href="/safety-ethics/high-altitude-medical-protocols-evacuation" class="nav-link" style="color: var(--color-accent); font-weight: 700; margin-top: auto;">Review Protocols &rarr;</a>
              </div>
            </div>
          </div>
        </section>

        <!-- Section: Conclusion -->'''

    assert old_conc in content, 'Conclusion marker not found'
    content = content.replace(old_conc, new_related_and_conc)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print('SUCCESS: All internal links and companion hub added to September guide.')

if __name__ == '__main__':
    main()
