import glob, os, re

base_dir = r"c:\Users\user\Downloads\ABC Trek Website"
files = sorted(glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True))

html_snippet = '''  <!-- Floating Quick Actions: Scroll to Top & WhatsApp -->
  <aside class="floating-actions" aria-label="Quick Actions">
    <button type="button" class="btn-floating btn-scroll-top" id="scrollTopBtn" aria-label="Scroll to top" title="Scroll to top">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 19V5M5 12l7-7 7 7"/>
      </svg>
    </button>
    <a href="https://wa.me/9779818188459" class="btn-floating btn-whatsapp" id="whatsappBtn" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp" title="Chat on WhatsApp">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
        <path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.101-.477-.151-.678.15-.2.302-.778.98-.953 1.181-.176.201-.351.226-.652.076-.301-.151-1.272-.469-2.423-1.496-.896-.799-1.501-1.787-1.677-2.088-.175-.302-.019-.465.132-.615.136-.135.301-.352.451-.527.151-.176.201-.302.302-.503.101-.201.05-.377-.025-.528-.075-.151-.677-1.633-.928-2.236-.244-.588-.493-.508-.678-.517l-.578-.01c-.201 0-.527.075-.803.377s-1.055 1.03-1.055 2.513c0 1.482 1.08 2.914 1.23 3.115.151.2 2.126 3.247 5.151 4.553.72.31 1.282.496 1.72.636.723.23 1.381.197 1.901.12.58-.087 1.78-.727 2.031-1.431.251-.703.251-1.306.176-1.431-.075-.126-.276-.201-.577-.352z"/>
        <path d="M12.042 2C6.51 2 2.023 6.486 2.023 12.019c0 1.996.587 3.864 1.603 5.441L2 22.062l4.776-1.571c1.517.944 3.308 1.488 5.266 1.488 5.532 0 10.019-4.486 10.019-10.019 0-5.533-4.487-10.019-10.019-10.019zm0 18.238c-1.745 0-3.364-.537-4.708-1.455l-.338-.231-2.83.931.942-2.759-.253-.356c-1.026-1.442-1.57-3.155-1.57-4.908 0-4.664 3.794-8.458 8.458-8.458 4.663 0 8.458 3.794 8.458 8.458 0 4.663-3.795 8.458-8.458 8.458z"/>
      </svg>
    </a>
  </aside>
'''

updated = 0
for f in files:
    rel = os.path.relpath(f, base_dir)
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    if 'class="floating-actions"' in content or "floating-actions" in content:
        print(f"Skipping {rel}: already has floating-actions")
        continue
        
    pattern = re.compile(r'(\s*<script\s+[^>]*src=["\'][^"\']*nav\.js[^"\']*["\'][^>]*>\s*</script>)')
    match = pattern.search(content)
    if not match:
        print(f"ERROR: Could not find nav.js script tag in {rel}")
        continue
        
    script_str = match.group(0)
    replacement = "\n" + html_snippet + script_str
    new_content = content[:match.start()] + replacement + content[match.end():]
    
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(new_content)
    updated += 1
    print(f"Updated {rel}")

print(f"Total files updated with floating action buttons: {updated}")
