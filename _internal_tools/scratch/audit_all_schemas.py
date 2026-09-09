import glob
import re
import json

def audit():
    files = glob.glob('**/*.html', recursive=True)
    all_schemas = {}
    errors = []
    
    print("=== Scanning all HTML files for Schema.org JSON-LD blocks ===")
    for f in sorted(files):
        content = open(f, encoding='utf-8').read()
        matches = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"]>([\s\S]*?)</script>', content)
        if matches:
            all_schemas[f] = []
            for i, m in enumerate(matches):
                try:
                    data = json.loads(m.strip())
                    all_schemas[f].append(data)
                except Exception as e:
                    errors.append(f"JSON ERROR in {f} block {i}: {e}")
                    
    print(f"Total files with schema: {len(all_schemas)} / {len(files)}")
    if errors:
        print("ERRORS ENCOUNTERED:")
        for e in errors:
            print(" ", e)
        return
        
    print("\nVerified Schema Summary by File:")
    for f, blocks in all_schemas.items():
        print(f"\n--- {f} ---")
        for b in blocks:
            if '@graph' in b:
                for item in b['@graph']:
                    t = item.get('@type')
                    name = item.get('headline') or item.get('name') or item.get('jobTitle') or ''
                    print(f"  [@graph] {t:18} | {name[:45]}")
            else:
                t = b.get('@type')
                name = b.get('headline') or b.get('name') or ''
                print(f"  [Single] {t:18} | {name[:45]}")
                
    # Check for any .html in schema URLs
    print("\n=== Checking for .html in schema URLs ===")
    html_in_schema = []
    for f, blocks in all_schemas.items():
        raw = json.dumps(blocks)
        urls = re.findall(r'https?://[^\s",]+', raw)
        for u in urls:
            if '.html' in u:
                html_in_schema.append((f, u))
                
    if html_in_schema:
        print(f"WARNING: Found {len(html_in_schema)} URLs with .html:")
        for f, u in html_in_schema:
            print(f"  {f}: {u}")
    else:
        print("PASS: Zero .html extensions found in any schema URLs! All URLs are clean & canonical.")

if __name__ == '__main__':
    audit()
