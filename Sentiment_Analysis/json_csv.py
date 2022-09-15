import json
import csv


# Opening JSON file and loading the data
# into the variable data

data = [json.loads(line) for line in open('chatlog_replay_L1ZwMUuGjzY.json', 'r', encoding='utf8')]
# print(data)
# print(type(data))

# now we will open a file for writing
data_file = open('chat_log.csv', 'w', newline='', encoding="utf-8")

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for chats in data:
    if count == 0:
        # Writing headers of CSV file
        header = chats.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(chats.values())

data_file.close()
