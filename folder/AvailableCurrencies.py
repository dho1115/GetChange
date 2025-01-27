'''
AvailableCurrencies.py will show all the available currencies your currency entry can be coverted to.
'''

from functions import MoneyChanger;

TwentyDollar = MoneyChanger('20 Dollar Bill', None, None)
TenDollar = MoneyChanger('10 Dollar Bill', '20 Dollar Bill', 2)
FiveDollar = MoneyChanger('5 Dollar Bill', '10 Dollar Bill', 2)
OneDollar = MoneyChanger('1 Dollar Bill', '5 Dollar Bill', 5)
Quarter = MoneyChanger('Quarter', '1 Dollar Bill', 4)
Nickel = MoneyChanger('Nickel', 'Quarter', 5)
Penny = MoneyChanger('Penny', 'Nickel', 5)

AllCurrencies = [TwentyDollar, TenDollar, FiveDollar, OneDollar, Quarter, Nickel, Penny];