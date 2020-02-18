# ==== request ====

import requests

#http://www.nbrb.by/API/ExRates/Currencies[/{Cur_ID}]
#http://www.nbrb.by/api/exrates/rates?periodicity=0

uri = 'http://www.nbrb.by/api/exrates/rates?periodicity=0'

resp = requests.get(uri)

if resp.status_code == 200:
    dict_list = resp.json()

curr_list = {}
for dict in dict_list:
    for key in dict:
        id = dict['Cur_Abbreviation']
        curr_list[id] = dict['Cur_ID']

j = 0
print("Available currencies:")
for i in list(curr_list.keys()):
    print(i, end=" ")
    j += 1
    if j % 10 == 0:
        print('')
print("\n")

# ==== user input ====

amount = input("Input amount: ")
curr1 = input("Input currency 1: ").upper()
curr2 = input("Input currency 2: ").upper()

print(f'\nConversion of {amount} {curr1} to {curr2}:')

def is_digit(n):
    if n.isdigit():
        return True
    else:
        try:
            float(n)
            return True
        except ValueError:
            return False


def is_rated(curr):
    if curr != 'BYN' and curr not in curr_list:
        print("This currency is not rated")
        return False
    else:
        return True

if curr1 == curr2:
    print("These are two identical currencies")

is_rated(curr1)
is_rated(curr2)

if is_digit(amount):
    amount = float(amount)
    if amount <= 0:
        print("It's not a correct sum!")
else:
    print("It's not a number!")

# ==== exchange ====

def return_rate(curr):
    if curr == 'BYN':
        return 1
    else:
        for dict in dict_list:
            if dict["Cur_Abbreviation"] == curr:
               return dict['Cur_OfficialRate'] / dict['Cur_Scale']

rate1 = return_rate(curr1)
rate2 = return_rate(curr2)

result = amount * rate1 / rate2
print(round(result, 2))
