'''
AvailableCurrencies.py will show all the available currencies your currency entry can be coverted to.
'''

from functions import MoneyChanger;

# Add any NEW MonecyChanger() functions to AvailableCurrencyDict (below):

DictionaryOfAllCurrencies = dict(
   TwentyDollar = MoneyChanger('20 Dollar Bill', 2000, None, None),
   TenDollar = MoneyChanger('10 Dollar Bill', 1000, '20 Dollar Bill', 2),
   FiveDollar = MoneyChanger('5 Dollar Bill', 500, '10 Dollar Bill', 2),
   OneDollar = MoneyChanger('1 Dollar Bill', 100, '5 Dollar Bill', 5),
   Quarter = MoneyChanger('Quarter', 25, '1 Dollar Bill', 4),
   Nickel = MoneyChanger('Nickel', 5, 'Quarter', 5),
   Penny = MoneyChanger('Penny', 1, 'Nickel', 5)
) #Changed this to a dict so I don't have to Add new AvailableCurrencyDict then Add it AGAIN to AllCurrencies (below).

CurrenciesToUse = DictionaryOfAllCurrencies.values();