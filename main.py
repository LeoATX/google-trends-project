import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(str(response.read(), 'utf-8'))
print("Hello")
