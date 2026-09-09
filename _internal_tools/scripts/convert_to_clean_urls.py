import os
import glob
import re

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def clean_url_string(url, current_file_rel):
    # Don't touch external or non-html links
    if '.html' not in url:
        return url
    
    # Ignore mailto, tel, javascript, etc.
    if url.startswith(('mailto:', 'tel:', 'javascript:', '#')):
        return url

    # Canonical or full domain URLs
    if url.startswith(('http://', 'https://')):
        if 'abctrekinnepal.com' in url:
            path = url.replace('https://www.abctrekinnepal.com', '').replace('http://abctrekinnepal.com', '')
            base_part = path
            suffix = ''
            if '#' in base_part:
                base_part, anchor = base_part.split('#', 1)
                suffix = '#' + anchor
            if '?' in base_part:
                base_part, query = base_part.split('?', 1)
                suffix = '?' + query + suffix
            proj_path = base_part.strip('/')
            if proj_path in ('index.html', ''):
                return 'https://www.abctrekinnepal.com/' + suffix
            elif proj_path in ('treks/index.html', 'treks'):
                return 'https://www.abctrekinnepal.com/treks' + suffix
            elif proj_path.endswith('.html'):
                return 'https://www.abctrekinnepal.com/' + proj_path[:-5] + suffix
            return 'https://www.abctrekinnepal.com/' + proj_path + suffix
        return url

    # Relative internal links
    base_part = url
    suffix = ''
    if '#' in base_part:
        base_part, anchor = base_part.split('#', 1)
        suffix = '#' + anchor
    if '?' in base_part:
        base_part, query = base_part.split('?', 1)
        suffix = '?' + query + suffix

    if not base_part.endswith('.html'):
        return url

    curr_dir = os.path.dirname(current_file_rel).replace('\\', '/')
    if base_part.startswith('/'):
        proj_path = base_part.lstrip('/')
    elif curr_dir in ('', '.'):
        proj_path = base_part
    else:
        proj_path = os.path.normpath(os.path.join(curr_dir, base_part)).replace('\\', '/')

    if proj_path == 'index.html':
        return '/' + suffix
    elif proj_path in ('treks/index.html', 'treks'):
        return '/treks' + suffix
    elif proj_path.endswith('.html'):
        return '/' + proj_path[:-5] + suffix
    return url

def process_html_file(filepath):
    rel_path = os.path.relpath(filepath, ROOT_DIR).replace('\\', '/')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content

    # 1. Replace href attributes: href="something.html..." or href='something.html...'
    def href_replacer(match):
        delim = match.group(1)
        target = match.group(2)
        cleaned = clean_url_string(target, rel_path)
        return f'href={delim}{cleaned}{delim}'

    content = re.sub(r'href=([\"\'])([^\"\']*\.html[^\"\']*)\1', href_replacer, content)

    # 2. Replace canonical tag links if any remain
    def canonical_replacer(match):
        prefix = match.group(1)
        url = match.group(2)
        suffix = match.group(3)
        cleaned = clean_url_string(url, rel_path)
        return f'{prefix}{cleaned}{suffix}'

    content = re.sub(r'(<link\s+rel=[\"\']canonical[\"\']\s+href=[\"\'])([^\"\']+)([\"\'])', canonical_replacer, content)

    # 3. Replace og:url
    content = re.sub(r'(<meta\s+property=[\"\']og:url[\"\']\s+content=[\"\'])([^\"\']+)([\"\'])', canonical_replacer, content)

    # 4. Replace structured JSON-LD URLs
    def json_url_replacer(match):
        prefix = match.group(1)
        url = match.group(2)
        suffix = match.group(3)
        cleaned = clean_url_string(url, rel_path)
        return f'{prefix}{cleaned}{suffix}'

    content = re.sub(r'(\"url\"\s*:\s*[\"\'])(https?://abctrekinnepal\.com[^\"]*\.html[^\"]*)([\"\'])', json_url_replacer, content)

    if content != orig_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def process_sitemap():
    sitemap_path = os.path.join(ROOT_DIR, 'sitemap.xml')
    if not os.path.exists(sitemap_path):
        return
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content
    def loc_replacer(match):
        url = match.group(1)
        cleaned = clean_url_string(url, 'sitemap.xml')
        return f'<loc>{cleaned}</loc>'

    content = re.sub(r'<loc>([^<]+\.html)</loc>', loc_replacer, content)
    if content != orig_content:
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated sitemap.xml with clean URLs.")

def main():
    html_files = glob.glob(os.path.join(ROOT_DIR, '**/*.html'), recursive=True)
    updated_count = 0
    for hf in html_files:
        if process_html_file(hf):
            updated_count += 1
            print(f"Updated: {os.path.relpath(hf, ROOT_DIR)}")

    print(f"\nDone. Updated {updated_count} of {len(html_files)} HTML files.")
    process_sitemap()

if __name__ == '__main__':
    main()
