a = float(input("Input number 1: "))
 
if a % 2 == 0:
    print("Odd")
    if a in range(2,28):
        print("In first range")
    elif a in range(29,54):
        print("In second range")
else:
    print("It's something")
