import urllib.request

urls = [
    'http://127.0.0.1:8080/',
    'http://127.0.0.1:8080/blog.html',
    'http://127.0.0.1:8080/treks/annapurna-base-camp-classic-10-days.html',
    'http://127.0.0.1:8080/company/about-us.html',
    'http://127.0.0.1:8080/team/sugam-shrestha.html'
]

for u in urls:
    res = urllib.request.urlopen(u)
    data = res.read().decode('utf-8')
    has_btn = 'class="floating-actions"' in data
    has_scroll = 'id="scrollTopBtn"' in data
    has_wa = 'id="whatsappBtn"' in data
    print(f'{u}: status={res.status}, floating_actions={has_btn}, scrollBtn={has_scroll}, whatsappBtn={has_wa}')
