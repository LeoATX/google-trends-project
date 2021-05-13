import pytrends.request
import requests


# Currently only takes one keyword
# Could add optional "start_datetime: datetime, end_datetime: datetime"
def get(keyword: str):
    client = pytrends.request.TrendReq(hl='en-US', tz=360)
    client.build_payload([keyword])
    data_frame_object = client.interest_over_time()
    fetched_csv = data_frame_object.to_csv()

    fetched_csv = str(fetched_csv)

    # Create a list to iterate the csv
    csv_iterable = ['']

    # Creates a list for final numerical output
    list_values = []

    # Loop through the csv file and add every row into csv_iterable
    row_count = 0
    for character in fetched_csv:
        if character != '\n':
            csv_iterable[row_count] += character
        if character == '\n':
            row_count += 1
            csv_iterable.append('')

    # Delete the last element
    del csv_iterable[len(csv_iterable) - 1]

    # Loop through each row and grab the value from the middle
    row_count = 0
    for row in csv_iterable:
        # Get rid of the first row
        if row_count == 0:
            row_count += 1
            continue

        row_list = ['']
        mini_list_count = 0
        for character in row:
            if character != ',':
                row_list[mini_list_count] += character
            if character == ',':
                row_list.append('')
                mini_list_count += 1

        list_values.append(row_list[1])

    # Change it to numerical
    for index in range(len(list_values) - 1):
        list_values[index] = float(list_values[index])

    return list_values


url = 'https://trends.google.com/trends/explore?q=Coronavirus'
headers = {'headers': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:88.0) Gecko/20100101 Firefox/88.0'}
response = requests.Session().get(url=url, headers=headers)
print(response.content)
