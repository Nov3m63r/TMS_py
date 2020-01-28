# x = []
# for i in range(1, 11):
#     x.append(i)
#
# data = [['a', 1], ['b', 2], ['c', 3]]
#
# x = [i + 1 for i in range(10)]
# y = {k: v for k, v in data}
#
# print(y)


# data = ['a', 'b', 'c', 'd']
#
# # [[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd']]
# y = {k: v + 1 for v, k in enumerate(data)}
# print(y)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# result = [element for row in matrix for element in row]
result = [[element + 1 for element in row] for row in matrix]
print(result)

# result = []
# for row in matrix:
#     for element in row:
#         result.append(element)
# print(result)
