import requests
from decimal import *
from datetime import datetime
getcontext().prec = 2


def currency_rates(currency):
    currency = currency.upper()
    site_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if currency not in site_str:
        return None
    rub = site_str[site_str.find('<Value>', site_str.find(currency)) + 7:site_str.find('</Value>', site_str.find(currency))]
    day_raw = site_str[site_str.find('Date="') + 6:site_str.find('"', site_str.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)
    return f'{Decimal(rub.replace(",", "."))}, {datetime(day=day, month=month, year=year)}'


print(currency_rates(str(input('Введите валюту: ', ))))

"""
    На сколько я понял decimal определяет количество знаков после запятой правильно округляя. Но в данной задаче цели округлить нет. 
Кроме того хоть никокой ошибки выполнение программы не выдает, но decimal не работает. Если я ставлю getcontext().prec = 2 то результат
всеравно идет с 4 знаками после запятой. 
Я часа 2 убил на то что бы понять почему не округляет, но до меня так и не дошло. Переписывал кучу раз программу и всеравно 4 знака 
после запятой...
"""


