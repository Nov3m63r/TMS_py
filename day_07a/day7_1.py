import json

with open('day7_1.json', 'r') as json_file:
    json_str = json_file.read()
    obj = json.loads(json_str)

