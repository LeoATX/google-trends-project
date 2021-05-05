import urllib.error
import urllib.request
import pytrends.request
import random
import multiprocessing

try:
    response = urllib.request.urlopen('https://trends.google.com/trends/explore?q=%2Fm%2F04n3w2r&geo=US.json')
    print(response)
except urllib.error.HTTPError:
    print(urllib.error.HTTPError)

client = pytrends.request.TrendReq(hl='en-US', tz=360)
client.build_payload(["Coronavirus"])
data_frame_object = client.interest_over_time()
csv = data_frame_object.to_csv()
print(csv)


def sort(unsorted: list):
    for indexa in range(len(unsorted) - 1):
        if unsorted[indexa] <= unsorted[indexa + 1]:
            continue
        if unsorted[indexa] > unsorted[indexa + 1]:
            swap = unsorted.pop(indexa)
            unsorted.insert(indexa, swap)
            del swap

    return unsorted


# Stress testing
print(random.random())
cycle = 0

# Add 100 random decimals to the list
while cycle <= 2000:
    stress_matrix = list()
    for loop in range(6):
        stress_matrix.append(list())

    for loop in range(10000):
        stress_matrix[0].append(random.random())

    p0 = multiprocessing.Process(target=stress_matrix[0].sort())
    p0.run()

    p1 = multiprocessing.Process(target=stress_matrix[1].sort())
    p1.run()

    p2 = multiprocessing.Process(target=stress_matrix[2].sort())
    p2.run()

    p3 = multiprocessing.Process(target=stress_matrix[3].sort())
    p3.run()

    p4 = multiprocessing.Process(target=stress_matrix[4].sort())
    p4.run()

    p5 = multiprocessing.Process(target=stress_matrix[5].sort())
    p5.run()

    cycle += 1

fib = [1, 1]
index = 2
while True:
    fib.append(fib[index - 1] + fib[index - 2])
    print(fib[index])
    index += 1
