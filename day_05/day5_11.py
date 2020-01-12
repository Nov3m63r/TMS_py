num = input("Input numbers: ").split()

for i in range(len(num)):
    print(type(i))
    num[i] = int(num[i])

def mult(n):
    res = 1
    if len(n) <= 1:
        print(res * n[0])
        return res * n[0]
    else:
        print(n[1:])
        return mult(n[1:])

print(mult(num))