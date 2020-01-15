num = input("Input numbers: ").split()

for i in range(len(num)):
<<<<<<< HEAD
    num[i] = int(num[i])

def mult(n):
    if len(n) > 1:
       n[0] *= mult(n[1:])
    return n[0]
        
print(mult(num))
=======
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
>>>>>>> 9b2bf65cef4eef6d8786ce13db94c32cf9c61207
