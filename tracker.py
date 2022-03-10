# Copyright (C) Yashasvi Baneswar Mishra - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Yashasvi Baneswar Mishra <yashasvimishra1@gmail.com>, March 2022
 


import requests
import time
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import requests
import sys
import time
import random
import datetime
import telepot
import os
import random
import telepot
from telepot.loop import MessageLoop
import pandas as pd
import datetime as dt
import plotly.express as px
import plotly.graph_objects as go
import requests
from datetime import datetime, timezone
import os
from PIL import Image
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import dootbot


# global variables
api_key = 'APPROPRIATE API KEY FROM A SERVICE OF YOUR CHOICE'   
bot_token = 'YOUR TELEGRAM BOT TOKEN'  
chat_id = ('YOUR CHAT ID') # YOU CAN ADD MULITPLE CHAT IDS SEPARATED BY COMMAS, ENCLOSED WITHIN SINGLE INVERTED COMMAS
threshold = 45000
time_interval = 30  
def get_btc_price():   
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'   
    headers = {  
        'Accepts': 'application/json',  
        'X-CMC_PRO_API_KEY': api_key 
    }
    # make a request to the coinmarketcap api
    response = requests.get(url, headers=headers) 
    response_json = response.json() 
# extract the bitcoin price from the json data
    btc_price = response_json['data'][0]  
    return btc_price['quote']['USD']['price'] 
# fn to send_message through telegram
def send_message(chat_id, msg): 
    for i in chat_id:
        url = 'https://api.telegram.org/bot{}/sendMessage'.format(bot_token)
        payload = {'chat_id': i, 'text': msg}
        response = requests.post(url, json=payload)
        print(response.json())

    # url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}" 


# send the msg 
    requests.get(url) 
# main function
def main():
    price_list = []
# infinite loop
    while True:
        price = get_btc_price()
        price_list.append(price)
# if the price falls below threshold, send an immediate msg
        if price < threshold:
            send_message(chat_id=chat_id, msg=f'BTC Price Drop Alert: {price}')
# send last 6 btc price
        if len(price_list) >= 5:
            send_message(chat_id=chat_id, msg=price_list)
            # empty the price_list
            price_list = []
# fetch the price for every dash minutes
        time.sleep(time_interval)


def get_prices():
    coins = ["BTC", "ETH", "XRP", "LTC", "BCH",
             "ADA", "DOT", "LINK", "BNB", "XLM"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"]
        }

    return data
    send_message(chat_id=chat_id, msg=f'BTC Price Drop Alert: {data}')


# fancy way to activate the main() function
if __name__ == '__main__':
    main()
 




















