# v.1
def func(*args):
    a = list(args)
    b = a.index(max(a))
    a.remove(a[b])
    return max(a)
   
print(func(2, 4, 6, 8, 10))


# v.2

num = input("Input numbers: ")
n = num.split()
q = []

for i in n:
    q = q.append(int(i))

print(q)

def func(*args):
    a = list(args)
    b = a.index(max(a))
    a.remove(a[b])
    return max(a)
   
#print(func(q))


