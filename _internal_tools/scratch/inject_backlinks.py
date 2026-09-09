import re

def update_guide_pillar():
    path = 'guide/annapurna-base-camp-trek.html'
    content = open(path, encoding='utf-8').read()
    
    # 1. Seasons callout
    target_str = '''            <div class="fact-tile">
              <div class="fact-title" style="color: #059669;">Spring (Mar – May) · Rhododendron Bloom</div>
              <div class="fact-data" style="font-size: 1.1rem;">Wildflowers & Warmer Temperatures</div>
              <p style="font-size: var(--text-caption); color: var(--color-text-muted); margin-top: 4px; margin-bottom: 0;">
                The hillsides between Ghorepani, Tadapani, and Chhomrong explode with vibrant red and pink rhododendron blooms. Mornings are clear with occasional afternoon cloud build-up.
              </p>
            </div>
          </div>'''
    
    replacement_str = '''            <div class="fact-tile">
              <div class="fact-title" style="color: #059669;">Spring (Mar – May) · Rhododendron Bloom</div>
              <div class="fact-data" style="font-size: 1.1rem;">Wildflowers & Warmer Temperatures</div>
              <p style="font-size: var(--text-caption); color: var(--color-text-muted); margin-top: 4px; margin-bottom: 0;">
                The hillsides between Ghorepani, Tadapani, and Chhomrong explode with vibrant red and pink rhododendron blooms. Mornings are clear with occasional afternoon cloud build-up.
              </p>
            </div>
          </div>

          <div style="margin: var(--space-20) 0; padding: var(--space-16) var(--space-20); background: rgba(249, 115, 22, 0.08); border-left: 4px solid var(--color-accent); border-radius: 0 var(--radius-md) var(--radius-md) 0;">
            <div style="font-weight: 700; color: var(--color-brand-dark); margin-bottom: 4px;">Planning an Early Autumn Departure?</div>
            <p style="margin: 0; font-size: var(--text-body-sm); color: var(--color-text-body); line-height: 1.6;">
              Wondering if September is the right window for your trek? Read our dedicated field intelligence: <a href="/guide/annapurna-base-camp-trek-september" style="color: var(--color-accent); font-weight: 700; text-decoration: underline;">Annapurna Base Camp Trek in September: Weather, Trails, Costs &amp; Itinerary Guide &rarr;</a>
            </p>
          </div>'''
    
    assert target_str in content, 'Target in pillar guide not found'
    content = content.replace(target_str, replacement_str)
    
    # 2. Footer link
    footer_target = '''            <li><a href="/guide/annapurna-base-camp-trek" class="footer-link">Ultimate ABC Guide (2026)</a></li>
            <li><a href="/blog" class="footer-link">Annapurna Field Blog</a></li>'''
            
    footer_repl = '''            <li><a href="/guide/annapurna-base-camp-trek" class="footer-link">Ultimate ABC Guide (2026)</a></li>
            <li><a href="/guide/annapurna-base-camp-trek-september" class="footer-link">ABC Trek in September</a></li>
            <li><a href="/blog" class="footer-link">Annapurna Field Blog</a></li>'''
            
    assert footer_target in content, 'Footer target in pillar guide not found'
    content = content.replace(footer_target, footer_repl)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated guide/annapurna-base-camp-trek.html')

def update_10day_trek():
    path = 'treks/annapurna-base-camp-classic-10-days.html'
    content = open(path, encoding='utf-8').read()
    
    target_str = '''          <p>
            Unlike rushed 6-day or 7-day itineraries that push trekkers recklessly up the steep Modi Khola gorge, our 10-day pacing ensures your body acclimatizes gradually through the subtropical rhododendron forests, Gurung stone villages, and subalpine bamboo zones before sleeping at Deurali (3,230m) and advancing into Annapurna Base Camp (4,130m).
          </p>'''
          
    replacement_str = '''          <p>
            Unlike rushed 6-day or 7-day itineraries that push trekkers recklessly up the steep Modi Khola gorge, our 10-day pacing ensures your body acclimatizes gradually through the subtropical rhododendron forests, Gurung stone villages, and subalpine bamboo zones before sleeping at Deurali (3,230m) and advancing into Annapurna Base Camp (4,130m).
          </p>

          <div style="margin: var(--space-20) 0; padding: var(--space-16) var(--space-20); background: rgba(249, 115, 22, 0.08); border-left: 4px solid var(--color-accent); border-radius: 0 var(--radius-md) var(--radius-md) 0;">
            <div style="font-weight: 700; color: var(--color-brand-dark); margin-bottom: 4px;">Planning a September Trek?</div>
            <p style="margin: 0; font-size: var(--text-body-sm); color: var(--color-text-body); line-height: 1.6;">
              Read our comprehensive seasonal dossier on late-monsoon trail clearing, weather transitions, and packing requirements: <a href="/guide/annapurna-base-camp-trek-september" style="color: var(--color-accent); font-weight: 700; text-decoration: underline;">Annapurna Base Camp Trek in September: Weather, Trails, Costs &amp; Itinerary &rarr;</a>
            </p>
          </div>'''
          
    assert target_str in content, 'Target in 10-day trek not found'
    content = content.replace(target_str, replacement_str)
    
    # Footer link
    footer_target = '''            <li><a href="/guide/annapurna-base-camp-trek" class="footer-link">Ultimate ABC Guide (2026)</a></li>
            <li><a href="/blog" class="footer-link">Annapurna Field Blog</a></li>'''
            
    footer_repl = '''            <li><a href="/guide/annapurna-base-camp-trek" class="footer-link">Ultimate ABC Guide (2026)</a></li>
            <li><a href="/guide/annapurna-base-camp-trek-september" class="footer-link">ABC Trek in September</a></li>
            <li><a href="/blog" class="footer-link">Annapurna Field Blog</a></li>'''
            
    assert footer_target in content, 'Footer target in 10-day trek not found'
    content = content.replace(footer_target, footer_repl)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated treks/annapurna-base-camp-classic-10-days.html')

def update_index():
    path = 'index.html'
    content = open(path, encoding='utf-8').read()
    
    # 1. Blog card 2
    card_target = '''        <div class="blog-card">
          <div class="blog-card-content">
            <span class="eyebrow">Climate & Seasons</span>
            <h3 class="blog-card-title">
              <a href="/guide/annapurna-base-camp-trek#seasons">Best Time to Trek Annapurna Base Camp</a>
            </h3>
            <p class="blog-card-excerpt">
              Month-by-month temperature breakdown, mountain clarity reports, snow line risks, and seasonal booking windows for Autumn and Spring.
            </p>
            <a href="/guide/annapurna-base-camp-trek#seasons" class="nav-link" style="color: var(--color-accent); font-weight: 700; margin-top: auto;">Explore Weather Matrix &rarr;</a>
          </div>
        </div>'''
        
    card_repl = '''        <div class="blog-card">
          <div class="blog-card-content">
            <span class="eyebrow">Climate & Seasons</span>
            <h3 class="blog-card-title">
              <a href="/guide/annapurna-base-camp-trek-september">ABC Trek in September: Complete Field Guide</a>
            </h3>
            <p class="blog-card-excerpt">
              Monsoon transition timelines, rainfall patterns, temperature gradients from Pokhara to 4,130m, packing gear, and cost breakdown.
            </p>
            <a href="/guide/annapurna-base-camp-trek-september" class="nav-link" style="color: var(--color-accent); font-weight: 700; margin-top: auto;">Explore September Guide &rarr;</a>
          </div>
        </div>'''
        
    assert card_target in content, 'Card target in index.html not found'
    content = content.replace(card_target, card_repl)
    
    # 2. Footer link
    footer_target = '''            <li><a href="/guide/annapurna-base-camp-trek" class="footer-link">Ultimate ABC Guide (2026)</a></li>
            <li><a href="/blog" class="footer-link">Annapurna Field Blog</a></li>'''
            
    footer_repl = '''            <li><a href="/guide/annapurna-base-camp-trek" class="footer-link">Ultimate ABC Guide (2026)</a></li>
            <li><a href="/guide/annapurna-base-camp-trek-september" class="footer-link">ABC Trek in September</a></li>
            <li><a href="/blog" class="footer-link">Annapurna Field Blog</a></li>'''
            
    assert footer_target in content, 'Footer target in index.html not found'
    content = content.replace(footer_target, footer_repl)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated index.html')

if __name__ == '__main__':
    update_guide_pillar()
    update_10day_trek()
    update_index()
    print('All backlinks successfully injected!')
