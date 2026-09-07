import glob
import re
import urllib.request
import urllib.parse
import os

BASE_URL = 'http://127.0.0.1:8080'

def test_all_links():
    html_files = glob.glob('**/*.html', recursive=True)
    all_links = set()
    
    for f in html_files:
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        hrefs = re.findall(r'href=[\"\']([^\"\']+)[\"\']', content)
        for h in hrefs:
            if h.startswith(('tel:', 'mailto:', 'javascript:', '#')):
                continue
            if h.startswith(('http://', 'https://')):
                if 'abctrekinnepal.com' in h:
                    parsed = urllib.parse.urlparse(h)
                    all_links.add(parsed.path)
                continue
            # Internal relative or absolute path
            path = h.split('?')[0].split('#')[0]
            if path:
                if not path.startswith('/'):
                    # relative
                    curr_dir = os.path.dirname(f).replace('\\', '/')
                    path = '/' + os.path.normpath(os.path.join(curr_dir, path)).replace('\\', '/')
                all_links.add(path)

    print(f"Total unique internal links to test: {len(all_links)}")
    
    errors = []
    successes = 0
    for link in sorted(all_links):
        url = BASE_URL + link
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req)
            if res.status in (200, 301, 302):
                successes += 1
            else:
                errors.append((link, res.status))
        except urllib.error.HTTPError as e:
            errors.append((link, e.code))
        except Exception as e:
            errors.append((link, str(e)))

    print(f"Successful links tested: {successes}")
    if errors:
        print(f"Errors found ({len(errors)}):")
        for link, err in errors:
            print(f"  {link} -> {err}")
    else:
        print("ALL INTERNAL LINKS RETURN 200 OK! Zero broken links.")

if __name__ == '__main__':
    test_all_links()
