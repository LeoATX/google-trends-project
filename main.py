import urllib.error
import urllib.request
import pytrends.request
import csv

try:
    response = urllib.request.urlopen('https://trends.google.com/trends/explore?q=%2Fm%2F04n3w2r&geo=US.json')
    print(response)
except urllib.error.HTTPError:
    print(urllib.error.HTTPError)

client = pytrends.request.TrendReq(hl='en-US', tz=360)
client.build_payload(["Coronavirus"])
data_frame_object = client.interest_over_time()
fetched_csv = data_frame_object.to_csv()

spamreader = csv.reader(fetched_csv)
for row in spamreader:
    print(', '.join(row))

print(spamreader)
