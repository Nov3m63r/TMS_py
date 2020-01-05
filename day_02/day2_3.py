while True:
    try:
        a = float(input("Input number 1: "))
        break
    except ValueError:
        print("Oops! Thatwas not a valid number. Try again: ")
while True:
    try:
        b = float(input("Input number 2: "))
        break
    except ValueError:
        print("Oops! Thatwas not a valid number. Try again: ")


print(int(a % b))
print(a / b)
