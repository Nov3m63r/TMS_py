import json


x = {'name': 'Alex', 'age': 20, 'subjects': [{'title': 'Python', 'mark': 10}, {'title': 'C++', 'mark': 9}]}
print(json.dumps(x, indent=4))
