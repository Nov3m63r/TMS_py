import re

str = "Windows Defender might be impacting your build performance. PyCharm checked the following directories"

# регулярные выражения
s = re.split(r" ", str)
print(s[0])

# методы строк, вар. 1
#s = str.split()
#print(s[0])

# методы строк, вар. 2
#s = str.find(" ")
#print(str[0:s])

