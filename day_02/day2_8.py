num = int(input("Input number: "))
lst = list(range(1, num+1))
print(lst)

# recursion

def one(numlist): 
    if len(numlist) == 1: 
        return numlist[0]
    else: 
        print(numlist)
        return one(numlist[::2])
         
print(one(lst))

