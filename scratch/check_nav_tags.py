import glob, os, re

files = sorted(glob.glob('**/*.html', recursive=True))

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    m = re.search(r'<script\s+[^>]*src=["\'][^"\']*nav\.js[^"\']*["\'][^>]*>\s*</script>', content)
    if m:
        print(f"{f:<50}: FOUND -> {m.group(0)}")
    else:
        print(f"{f:<50}: NOT FOUND!")
