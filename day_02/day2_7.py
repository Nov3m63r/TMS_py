a = input("Input word 1: ")
b = input("Input word 2: ")

def reverse (word):
    rev = []
    for i in word.lower()[::-1]:
        rev.append(i)
    return rev

print(reverse(a))
print(reverse(b))
