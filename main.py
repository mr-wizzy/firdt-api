# * imports all the classes in the tkinter module
from tkinter import *
import tkinter as tk
import requests 
import json


cryptoApi = Tk()
#it titles my gui.
cryptoApi.title("My first Portfolio App")




def myPortfolio():
  
      #get gives us information from our database
      my_api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=NGN&CMC_PRO_API_KEY=3889ce63-c733-403d-8b7d-c41a2438b4ea")
      #using .load here helps us to convert json data to python strings and .content makes it to display on screen
      api = json.loads(my_api_request.content)
      print("----------------")
      print("----------------")
      #my dictionary that stores all my crypto assets.
      crypto = [
        {
          "symbol":"BTC",
          "amount_owned": 2,
          "price_per_coin": 3200
        }, 
        {
          "symbol":"EOS",
          "amount_owned": 100,
          "price_per_coin": 2.05
        }
      ]
      #variable to store my total profits and loss. changes as the value gets added
      all_pro_los = 0
      #for loop for going through my first five assets and checking if it is contained in my dictionary of owned assets
      for assets in range(0, 5):
        for coin in crypto:
          if api["data"][assets]["symbol"] == coin["symbol"]:
            total_paid = coin["amount_owned"] * coin["price_per_coin"]
            #calculation to get my current value of each coin
            current_value = coin["amount_owned"] * api["data"][assets]["quote"]["NGN"]["price"]
            #to get my profit and loss
            pl_percoin = api["data"][assets]["quote"]["NGN"]["price"] - coin["price_per_coin"]
            all_pl_coin = pl_percoin * coin["amount_owned"]
            #this gets my total profit and loss
            all_pro_los = all_pro_los + all_pl_coin

            print(api["data"][assets]["name"] + " - " + api["data"][assets]["symbol"])
            print("Price - N{0:.2f}".format(api["data"][assets]["quote"]["NGN"]["price"]))
            print("Number Of Coin:", coin["amount_owned"])
            print("Total Amount Paid:", "N{0:.2f}".format(total_paid))
            print("Current Value:", "N{0:.2f}".format(current_value))
            print("P/L Per Coin:", "N{0:.2f}".format(pl_percoin))
            print("Total P/L With Coin:", "N{0:.2f}".format(all_pl_coin))
            print("----------------")

      print("Total P/L For Portfolio:", "N{0:.2f}".format(all_pro_los))

name = Label(cryptoApi, text="Coin Name", bg="purple", fg="white")
name.grid(row=0, column=0, sticky=N+S+E+W)

cost = Label(cryptoApi, text="Price", bg="white", fg="black")
name.grid(row=0, column=1, sticky=N+S+E+W)

numOwned = Label(cryptoApi, text="Amount Owned", bg="purple", fg="white")
name.grid(row=0, column=2, sticky=N+S+E+W)

numPaid = Label(cryptoApi, text="Total Amount Paid", bg="white", fg="black")
name.grid(row=0, column=3, sticky=N+S+E+W)

value = Label(cryptoApi, text="Current Value", bg="purple", fg="white")
name.grid(row=0, column=4, sticky=N+S+E+W)

plCoin = Label(cryptoApi, text="P/L Per Coin", bg="white", fg="black")
name.grid(row=0, column=5, sticky=N+S+E+W)

totalPL = Label(cryptoApi, text="Total P/L Per Coin", bg="purple", fg="white")
name.grid(row=0, column=6, sticky=N+S+E+W)

cryptoApi.mainloop()

print("My work is done")