a = [1, 2, 3, 5, 8, 13, 42, 5, 8]
b = [5, 8, 13, 42]

last_index = len(a) - len(b)
    
for i in range(last_index):
    n = i + len(b)
    if a[i:n] == b:
        print("True")
        break
    elif i == last_index:
        print("False")

#i = 0
#while i <= last_index:
#    n = i + len(b)
#    if a[i:n] == b:
#        print("True")
#        break
#    elif i == last_index:
#        print("False")
#    i += 1
