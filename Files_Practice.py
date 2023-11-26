
#Files - Note that none of these are going to work as we don't have the actual files...
with open("welcome.txt") as text_file:
  text_data = text_file.read()

print(text_data)

with open("how_many_lines.txt") as lines_doc:
  for lines in lines_doc:
    print(lines)

with open("just_the_first.txt") as first_line_doc: #default is for read only (note no second argument)
  first_line = first_line_doc.readline()

print(first_line)

with open("bad_bands.txt", 'w') as bad_bands_doc: #write 
  bad_bands_doc.write("Creed")

with open("cool_dogs.txt", "a") as cool_dogs_file: #append instead of write
  cool_dogs_file.write('Air Buddy\n')

import csv
isbn_list = []

with open("books.csv") as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter="@")
  for row in books_reader:
    isbn_list.append(row["ISBN"])
    #isbn_list.append(row['ISBN'])

print(isbn_list)


## Exporting to CSV
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open("logger.csv", "w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames = fields)
  log_writer.writeheader()
  for row in access_log:
    log_writer.writerow(row)

## Similar concepts with JSON
import json

with open("message.json") as message_json:
  message = json.load(message_json)
  print(message)

## Exporting JSON
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open("data.json", "w") as data_json:
  json.dump(data_payload, data_json)