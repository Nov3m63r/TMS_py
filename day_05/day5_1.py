num = (1, 5, 7, 2, 6, 4, 9, 25, 51, 14, 3)

def func(*args):
    lst = list(args)
    print(lst)
    #lst.remove(max(lst))
    #return max(lst)

func(num)

