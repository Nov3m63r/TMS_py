str = input("Input frase: ")

def func(s):
    words = s.split(" ")
    w = []
    if len(w) < 19:
        for i in words:
            w.append(i)
    print(w)

func(str)
