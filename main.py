'''
GetChangeApp:

Github repository: https://github.com/dho1115/GetChange
YouTube Link: https://youtu.be/BPSBH8beOEI

This app will take the number for ONE TYPE OF CURRENCY (e.g.: dollar bill, quarter, nickel, etc... ) and convert that one currency UP to the equivalent currency:

For Instance:
If you have 4 quarters, GetChangeApp will convert it to 1 dollar.
If you have 7 dollars, GetChangeApp will convert it to 1 5 dollar bill & 2 1 dollar bills.
Similarly, if you have 9 quarters, it will conver it to 2 1 dollar bills and 1 quarter.

IMPORTANT!!! GetChangeApp only converts UP. It does not convert down, so I cannot get, say, pennies for my quarters.
'''
from sys import path;
from os import getenv;
from dotenv import load_dotenv;
from colorama import init;
from termcolor import colored;
from pyfiglet import figlet_format;

init()
load_dotenv();

folderpath = getenv('folderroute') #Retrieve the path to my folder (otherwise, main.py CANNOT see my folder for some odd reason).
path.append(folderpath); #path will show the current paths my folder can view. By appending folderpath, I am adding a new path for my current directory (main.py).

if __name__ == "__main__":
   from functools import reduce;
   from folder.AvailableCurrencies import CurrenciesToUse;

   f = figlet_format('CHANGE-UP APP!!!');
   coloredFiglet = colored(f, 'light_green', attrs=['bold']);
   print(coloredFiglet);
   print()
   input("HIT ANY KEY TO CONTINUE.")

   Money:list = list(enumerate(CurrenciesToUse, 0)); #[(0, {...data}), (1, {...data}), (2, {...data}), etc...]

   AvailableEntries = [i['currency'] for i in CurrenciesToUse] #More dynamic and flexible than ["20 Dollar Bill", "10 Dollar Bill", "5 Dollar Bill", "1 Dollar Bill", "Quarter", "Nickel", "Penny"]

   #First Question.
   CurrencyEntry = input(f"Enter the currency you want to get change for: {AvailableEntries}: ");
   print("\n"*3)

   try:
      if CurrencyEntry not in AvailableEntries: raise ValueError(f"VALUE ERROR: {CurrencyEntry} is not in the list of availableEntries {AvailableEntries}!!!");
   
      #Second Question.
      quantity = input(f"How many {CurrencyEntry} do you have? ");
      print("\n"*3)

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
      MoneyDict = list(filter(lambda x: x['quantity'] > 0, list(x[1] for x in Money))) # I want to return ONLY currencies with quantity GREATER than 0. Hence, the x['quantity'] > 0.

      SortedMoney = reduce(lambda accumulator, value: {**accumulator, value["currency"]: value["quantity"]}, [dict(currency=i['currency'], quantity=i['quantity']) for i in MoneyDict], {}); #Puts everything into a dictionary format that will ***ONLY GIVE ME { currency: int > 0, quantity: int > 0 } ***. Optional. I think it looks better.

      print(f"For your {quantity} of {CurrencyEntry}, you will receive the following:");
      for i in SortedMoney.items():
         print(f"You will get {colored(i[1], 'yellow', attrs=['bold'])} {colored(i[0], 'light_green', attrs=['bold'])}") #The (colored) output.

   except (NameError, ValueError, TypeError) as err:
      print(f"\nERROR!!! Make sure your currency entry, {CurrencyEntry} is one of THESE VALUES: {AvailableEntries}. Currently, validation shows the following results as to whether {CurrencyEntry} is in {AvailableEntries}: {CurrencyEntry in AvailableEntries} \nAnother possibility is your quantity entered, {quantity} CANNOT be turned into an integer.\n- {err}.");

   except Exception as exc:
      print(f"EXCEPTION!!! {exc} - {exc.args}.")   


