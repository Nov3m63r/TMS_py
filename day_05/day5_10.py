num = int(input("Input number: "))

def sum (n):
    if n > 1:
        n += sum(n - 1)
    return n

print(sum(num))
