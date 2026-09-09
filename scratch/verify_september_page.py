import urllib.request

url = 'http://127.0.0.1:8080/guide/annapurna-base-camp-trek-september.html'
try:
    res = urllib.request.urlopen(url)
    data = res.read().decode('utf-8')
    print('HTTP status:', res.status)
    print('Page title found:', 'Annapurna Base Camp Trek in September' in data)
    print('Floating actions found:', 'floating-actions' in data)
    print('Byte length:', len(data))
    print('FAQ count:', data.count('class="faq-item"'))
    print('Table count:', data.count('<table'))
    print('Stepper day count:', data.count('stepper-day-card'))
except Exception as e:
    print('Error:', e)
