import json
# from decimal import Decimal
#
# data = {
#     'name': 'Alex',
#     'age': 24,
#     'marks': [7, 10, 9, 8, {'a': [1, 2, 3, [1, 2, [3]]]}],
#     'None': None,
# }
#
# with open('json_file.txt', 'w') as json_file:
#     json_str = json.dumps(data)
#     print(json_str)
#     json_file.write(json_str)


with open('json_file_2.txt', 'r') as json_file:
    json_str = json_file.read()
    obj = json.loads(json_str)


with open('json_file_2.txt', 'r') as json_file:
    obj = json.load(json_file)
    print(obj)
