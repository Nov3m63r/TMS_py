import json
import csv

json_path = "json_file.json"
csv_path = "day7_1.csv"

with open(json_path) as json_file:
    f = json_file.read()
    json_str = json.loads(f)

keys = []
for line in json_str:
    key_line = list(dict.keys(line))
    for key in key_line:
        if key not in keys:
            keys.append(key)


with open(csv_path, "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(keys)

    for line in json_str:
        row = []
        for i in keys:
            row.append(dict.get(line, i))
        writer.writerow(row)

print("csv file is ready")