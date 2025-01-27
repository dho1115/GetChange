'''
AvailableCurrencies.py will show all the available currencies your currency entry can be coverted to.
'''

from functions import MoneyChanger;

# Add any NEW MonecyChanger() functions to AvailableCurrencyDict (below):

AvailableCurrencyDict = dict(
   TwentyDollar = MoneyChanger('20 Dollar Bill', None, None),
   TenDollar = MoneyChanger('10 Dollar Bill', '20 Dollar Bill', 2),
   FiveDollar = MoneyChanger('5 Dollar Bill', '10 Dollar Bill', 2),
   OneDollar = MoneyChanger('1 Dollar Bill', '5 Dollar Bill', 5),
   Quarter = MoneyChanger('Quarter', '1 Dollar Bill', 4),
   Nickel = MoneyChanger('Nickel', 'Quarter', 5),
   Penny = MoneyChanger('Penny', 'Nickel', 5)
) #Changed this to a dict so I don't have to Add new AvailableCurrencyDict then Add it AGAIN to AllCurrencies (below).

AllCurrencies = AvailableCurrencyDict.values();