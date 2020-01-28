import datetime

d = datetime.datetime(2018, 5, 17, 14, 20, 00)
now = datetime.datetime.now()
delta = now - d

print(delta)

