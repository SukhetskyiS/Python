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
