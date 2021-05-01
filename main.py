import urllib.request
import urllib.error
import pytrends.request

try:
    response = urllib.request.urlopen('https://trends.google.com/trends/explore?q=Coronavirus&geo=US')
    print(response)
except urllib.error.HTTPError:
    print(urllib.error.HTTPError)

print("=========PYTRENDS=========")
client = pytrends.request.TrendReq(hl='en-US', tz=360)
client.build_payload(["Hello"])
print(client.interest_over_time())
