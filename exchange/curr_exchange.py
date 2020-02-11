#=======
#request
#=======

import requests

#http://www.nbrb.by/API/ExRates/Currencies[/{Cur_ID}]
#http://www.nbrb.by/api/exrates/rates?periodicity=0

uri = 'http://www.nbrb.by/API/ExRates/Currencies'

resp = requests.get(uri)

if resp.status_code == 200:
    dict_list = resp.json()

# print(type(dict))
# print(resp.json())
    # Cur_ID
    # Cur_Code
    # Cur_Name

curr_list = {}
for dict in dict_list:
    for key, value in dict.items():
        #print(key, value)
        if key == 'Cur_ID':
            id = dict['Cur_ID']
            curr_list[id] = dict['Cur_Name']

print(curr_list)

#==========
#user input
#==========
curr_list_short = {19: 'Евро', 88: 'Монгольский тугрик', 108: 'Польский злотый', 141: 'Российский рубль',
             143: 'Фунт стерлингов', 145: 'Доллар США', 169: 'Украинская гривна', 171: 'Чешская крона',
             172: 'Эстонская крона',  177: 'Литовский лит', 180: 'Словацкая крона'}

amount, curr1, curr2 = input("Input amount, curr1, curr2: ")


def is_digit(n):
    if n.isdigit():
        return True
    else:
        try: 
            float(n) 
            return True 
        except ValueError: 
            return False


if is_digit(amount):
    amount = float(amount)
    print("ok")
    if amount <= 0:
        print("It's not a correct number!")
else:
    print("It's not a number!")



#========
#exchange
#========

#вычисления



