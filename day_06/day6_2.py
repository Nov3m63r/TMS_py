import re

str = "A Windows Defender might be impacting your build performance. PyCharm checked the following directories"

# методы строк
#s = str.split()
#for i in s:
#    if len(i) < 3:
#        i = i + "  "
#    print(i[:3])

# регулярные выражения
s = re.split(r" ", str)
#print(s)
#sss = re.findall(r"\S..", s)
for i in s:
    print(re.match(r"\S..", i))
