x = float(input("Input number 1: "))
y = float(input("Input number 2: "))
z = float(input("Input number 3: "))

a = True 
while a:
    x, y = y, x + y
    if y > z:
        a = False
        if y == z:
            print ("True")
        else:
            print ("False")     
