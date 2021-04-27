import urllib.request
import pytrends.request

# This gets the CSV file for League of Legends vs CSGO over the past year
response = urllib.request.urlopen('https://trends.google.com/trends/api/widgetdata/multiline/csv?req=%7B%22time%22%3A'
                                  '%222020-04-27%202021-04-27%22%2C%22resolution%22%3A%22WEEK%22%2C%22locale%22%3A'
                                  '%22en-US%22%2C%22comparisonItem%22%3A%5B%7B%22geo%22%3A%7B%22country%22%3A%22US%22'
                                  '%7D%2C%22complexKeywordsRestriction%22%3A%7B%22keyword%22%3A%5B%7B%22type%22%3A'
                                  '%22ENTITY%22%2C%22value%22%3A%22%2Fm%2F04n3w2r%22%7D%5D%7D%7D%2C%7B%22geo%22%3A%7B'
                                  '%22country%22%3A%22US%22%7D%2C%22complexKeywordsRestriction%22%3A%7B%22keyword%22'
                                  '%3A%5B%7B%22type%22%3A%22ENTITY%22%2C%22value%22%3A%22%2Fm%2F0h3pv2z%22%7D%5D%7D'
                                  '%7D%5D%2C%22requestOptions%22%3A%7B%22property%22%3A%22%22%2C%22backend%22%3A'
                                  '%22IZG%22%2C%22category%22%3A0%7D%7D&token'
                                  '=APP6_UEAAAAAYImuTaAPniNIwJ6CWyv4avj7oDa7MCXO&tz=300')
print(response.read())

# This gets the CSV file for Taylor Swift vs Kim Kardashian over the past week
response = urllib.request.urlopen('https://trends.google.com/trends/api/widgetdata/multiline/csv?req=%7B%22time%22%3A'
                                  '%222021-04-20T18%5C%5C%3A55%5C%5C%3A02%202021-04-27T18%5C%5C%3A55%5C%5C%3A02%22%2C'
                                  '%22resolution%22%3A%22HOUR%22%2C%22locale%22%3A%22en-US%22%2C%22comparisonItem%22'
                                  '%3A%5B%7B%22geo%22%3A%7B%22country%22%3A%22US%22%7D%2C'
                                  '%22complexKeywordsRestriction%22%3A%7B%22keyword%22%3A%5B%7B%22type%22%3A%22ENTITY'
                                  '%22%2C%22value%22%3A%22%2Fm%2F0dl567%22%7D%5D%7D%7D%2C%7B%22geo%22%3A%7B%22country'
                                  '%22%3A%22US%22%7D%2C%22complexKeywordsRestriction%22%3A%7B%22keyword%22%3A%5B%7B'
                                  '%22type%22%3A%22ENTITY%22%2C%22value%22%3A%22%2Fm%2F0261x8t%22%7D%5D%7D%7D%5D%2C'
                                  '%22requestOptions%22%3A%7B%22property%22%3A%22%22%2C%22backend%22%3A%22CM%22%2C'
                                  '%22category%22%3A0%7D%7D&token=APP6_UEAAAAAYImvhqOaJVFgZ735pfOnpxY7ZkLFdv8k&tz=300')
print(response.read())

client = pytrends.request.TrendReq(hl='en-US', tz=360)
client.build_payload(["Hello"])
print(client.interest_over_time())
