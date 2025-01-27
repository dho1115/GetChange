'''
GetChangeApp:
This app will take the number of change you have and convert it UP to the equivalent currency:

For Instance:
If you have 4 quarters, GetChangeApp will convert it to 1 dollar.
If you have 7 dollars, GetChangeApp will convert it to 1 5 dollar bill & 2 1 dollar bills.
Similarly, if you have 9 quarters, it will conver it to 2 1 dollar bills and 1 quarter.

IMPORTANT!!! GetChangeApp only converts UP. It does not convert down, so I cannot get, say, pennies for my quarters.
'''
from sys import path;
from os import getenv;
from dotenv import load_dotenv;

load_dotenv();

folderpath = getenv('folderroute') #Retrieve the path to my folder (otherwise, main.py CANNOT see my folder for some odd reason).
path.append(folderpath); #path will show the current paths my folder can view. By appending folderpath, I am adding a new path for my current directory (main.py).

if __name__ == "__main__":
   from functools import reduce;
   from folder import AvailableCurrencies;
   from folder.AvailableCurrencies import AllCurrencies;

   print(AvailableCurrencies.__doc__)

   def MoneyChanger(CurrentCurrent, NewCurrency, GetChangeAt):
      return dict(currency=CurrentCurrent, changeFor=NewCurrency, when=GetChangeAt, quantity=0);

   Money:list = list(enumerate(AllCurrencies, 0));

   AvailableEntries = ["20 Dollar Bill", "10 Dollar Bill", "5 Dollar Bill", "1 Dollar Bill", "Quarter", "Nickel", "Penny"];
   CurrencyEntry = input(f"Enter the currency you want to get change for: {AvailableEntries}: ");

   try:
      if CurrencyEntry not in AvailableEntries: raise ValueError(f"VALUE ERROR: {CurrencyEntry} is not in the list of availableEntries {AvailableEntries}!!!");

      quantity = input(f"How many {CurrencyEntry} do you have? ");

      if not isinstance(int(quantity), int): raise NameError();
      else: quantity = int(quantity);

      for i in range(quantity):
         '''
         KEY for Money[list(filter(lambda x: x[1]['currency'] == CurrencyEntry, Money))[0][0]][1]: 

         Money:list[enum] = [...(index:int, currency_details:dict)];
         x in lambda = (index:int, currency_details:dict);
         x[1] = {currency, changeFor, quantity, when};
         x[1]['currency'] = int.

         list(filter(lambda x: x[1]['currency'] == CurrencyEntry, Money)) = [(index, {...currency_details, currency: CurrencyEntry})]
         Money[int][int] = {...currency_details}.
         '''

         Money[list(filter(lambda x: x[1]['currency'] == CurrencyEntry, Money))[0][0]][1]['quantity']+=1;
         for object in Money:
            if (object[1]['quantity'] == object[1]['when']) and (object[1]['when'] != None):
               object[1]['quantity']-=object[1]['when'];
               GetChangeFor = object[1]['changeFor'];
               Money = list(map(lambda x: (x[0], {**x[1], 'quantity': x[1]['quantity'] + 1}) if x[1]['currency'] == GetChangeFor else x, Money));
      
      '''
      BELOW:
      MoneyDict = list(filter(lambda x: x['quantity'] > 0, list(x[1] for x in Money)))
      This function will leave out any currency with a quantity of zero.
      So, for instance... let's say you have 4 quarters. 
      Well, that is equivalent to 1 one dollar bill, zero five dollar bills and zero for any other currency.
      MoneyDict (function below) will NOT show those currency with zero quantities.
      '''
      MoneyDict = list(filter(lambda x: x['quantity'] > 0, list(x[1] for x in Money)))

      SortedMoney = reduce(lambda accumulator, value: {**accumulator, value["currency"]: value["quantity"]}, [dict(currency=i['currency'], quantity=i['quantity']) for i in MoneyDict], {}); #Puts everything into a dictionary format. Optional. I think it looks better.

      print(f"HERE IS YOUR CHANGE:\n{SortedMoney}");

   except NameError as ne:
      print(f"VALUE ERROR!!! One possibility for this is in your quantity entry.\nMake sure the quantity you have can be turned into an INTEGER. Can your entry, {quantity} be turned into an integer? Currently, the DATA TYPE for {quantity} is {type(quantity).__name__}\n- {ne}.");

   except TypeError as te:
      print(f"TYPE ERROR!!! Unable to convert your quantity entry, {quantity} into a number!!! - {te}.");

   except ValueError as ve:
      print(f"\nVALUE ERROR!!! Make sure your currency entry, {CurrencyEntry} is one of THESE VALUES: {AvailableEntries}. Currently, validation shows the following results as to whether {CurrencyEntry} is in {AvailableEntries}: {CurrencyEntry in AvailableEntries} \nAnother possibility is your quantity entered, {quantity} CANNOT be turned into an integer.\n- {ve}.");

   except Exception as exc:
      print(f"EXCEPTION!!! {exc} - {exc.args}.")




         
      


