#1_7

for i in range(-50, 378):
    if i % 3 == 0 and i % 7 == 0:
        print("foobar")
    elif i % 3 == 0:
        print("foo")
    elif i % 7 == 0:
        print("bar")
    else:
        print(i)