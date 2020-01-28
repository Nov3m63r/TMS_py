num = input("Input numbers: ").split()

for i in range(len(num)):
    num[i] = int(num[i])

def mult(n):
    if len(n) > 1:
       n[0] *= mult(n[1:])
    return n[0]
        
print(mult(num))

