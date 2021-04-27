import urllib.request

response = urllib.request.urlopen('https://trends.google.com/trends/explore?q=%2Fm%2F0dl567,%2Fm%2F0261x8t&date=now%207-d&geo=US')
print(str(response.read(), 'utf-8'))
