import urllib.request
import re
import os

BASE_URL = "http://127.0.0.1:8080"

def test_url(url_path):
    full_url = f"{BASE_URL}{url_path}"
    try:
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            return resp.status, resp.geturl()
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return str(e), None

def main():
    files_to_check = [
        'guide/annapurna-base-camp-trek-september.html',
        'guide/annapurna-base-camp-trek.html',
        'treks/annapurna-base-camp-classic-10-days.html',
        'index.html',
        'blog.html'
    ]
    
    all_clean_urls = set()
    errors = []
    
    print("=== 1. Checking for .html in internal hrefs ===")
    for fpath in files_to_check:
        content = open(fpath, encoding='utf-8').read()
        # Find all hrefs
        hrefs = re.findall(r'href=[\'"]([^\'"]+)[\'"]', content)
        for h in hrefs:
            if h.startswith('/') and not h.startswith('//'):
                # Exclude assets like /css/, /images/, /js/, /fonts/
                if not any(h.startswith(prefix) for prefix in ['/css', '/images', '/js', '/fonts', '/favicon']):
                    # Check if .html is in url
                    if '.html' in h:
                        errors.append(f"Found .html in {fpath}: {h}")
                    else:
                        all_clean_urls.add(h.split('#')[0])
                        
    if errors:
        print(f"FAILED: Found {len(errors)} URLs with .html:")
        for e in errors:
            print("  ", e)
    else:
        print(f"PASSED: No .html extensions found in internal links across {len(files_to_check)} files!")
        
    print(f"\n=== 2. Testing HTTP Status of {len(all_clean_urls)} unique internal clean URLs on dev server ===")
    status_fail = False
    for path in sorted(all_clean_urls):
        if not path:
            path = "/"
        status, final_url = test_url(path)
        status_str = f"HTTP {status}"
        if status == 200:
            print(f"  [OK 200] {path:65} --> {final_url}")
        else:
            print(f"  [FAIL {status}] {path:65}")
            status_fail = True
            
    if not status_fail:
        print("\nPASSED: ALL internal clean URLs respond with HTTP 200 OK!")
    else:
        print("\nFAILED: Some internal URLs returned errors.")

if __name__ == '__main__':
    main()
