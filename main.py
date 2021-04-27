import urllib.request

response = urllib.request.urlopen('https://trends.google.com/trends/explore?date=today%203-m&geo=US&q=%2Fm%2F04n3w2r,'
                                  '%2Fm%2F0h3pv2z')
print(str(response.read(), 'utf-8'))
