from collections import defaultdict


names = [
    'Anton', 'Kate', 'Alex',
    'John', 'Kate', 'Ann',
    'John', 'John'
]
result = defaultdict(int)
for name in names:
    result[name] += 1

# leader = None
# max_amount = 0
# for name, amount in result.items():
#     if amount > max_amount:
#         leader = name
#         max_amount = amount

# print(leader, max_amount)
# print(dict(result))

print(
    sorted(result.items(), key=lambda data: -data[1])[0]
)