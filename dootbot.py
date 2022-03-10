# Copyright (C) Yashasvi Baneswar Mishra - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Yashasvi Baneswar Mishra <yashasvimishra1@gmail.com>, March 2022

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_prices
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
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

telegram_bot_token = 'YOUR TELEGRAM BOTS TOKEN'

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def portfolio(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)


def csv(update, context):
    chat_id = update.effective_chat.id
    message = "sending the historic csv file uptill today"
    history = yf.download(tickers='BTC-USD', period = 'MAX', interval = '1d')
    history.to_csv(r'C:\Users\KIIT\Desktop\bitcoin_tracker\BTC-USD.csv')
    context.bot.send_message(chat_id=chat_id, text=message)
    context.bot.send_document(chat_id, document=open(r'C:\Users\KIIT\Desktop\bitcoin_tracker\BTC-USD.csv', 'rb'))

def forecast(update, context):
    chat_id = update.effective_chat.id
    message = "sending the forecast chart"
    context.bot.send_photo(chat_id, photo=open(r'C:\Users\KIIT\Desktop\bitcoin_tracker\1.png', 'rb'))


def version(update, context):
    chat_id = update.effective_chat.id
    message = "Welcome to CrytpoDoot! Version 1.0.0\n\n"
    message += "Software Maintainer: Yashasvi Baneswar Mishra (yashasvimishra1@gmail.com)\n\n"
    context.bot.send_message(chat_id=chat_id, text=message)

def qr(update, context):
    chat_id = update.effective_chat.id
    message = "sending the qr code"
    context.bot.send_photo(chat_id, photo=open(r'C:\Users\KIIT\Desktop\bitcoin_tracker\qr_cryptodoot.jpg', 'rb'))

def feedback(update, context):
    chat_id = update.effective_chat.id
    message = "Have any feedback, suggestions or bug reports? Feel free to mail the maintainer, Yashasvi Baneswar Mishra (yashasvimishra1@gmail.com)-\n\n"
    message += "Want to get into the Beta Developer/Tester group? Feel free to mail the Administrator -\n\n"
    message += "Admin: Yashasvi Baneswar Mishra (yashasvimishra1@gmail.com)\n\n"
    context.bot.send_message(chat_id=chat_id, text=message)


def dynamiccsv(update, context):
    chat_id = update.effective_chat.id
    message = "sending a dynamic csv file for today, of the last 24 hours, with a ticker set to 15 minutes"
    data = yf.download(tickers='BTC-USD', period = '24h', interval = '15m')
    data.to_csv(r'C:\Users\KIIT\Desktop\bitcoin_tracker\DYNAMIC_BTC-USD.csv')
    context.bot.send_message(chat_id=chat_id, text=message)
    context.bot.send_document(chat_id, document=open(r'C:\Users\KIIT\Desktop\bitcoin_tracker\DYNAMIC_BTC-USD.csv', 'rb'))

#---------------------/btcchart---------------------
import requests
res = requests.get('https://api.coingecko.com/api/v3/coins/lunadoge/market_chart?vs_currency=usd&days=1')
prices_res = res.json().get('prices')
telegram_bot_token = '5101284223:AAGuasvtgsxtypb9n4Eu8Kk7soGqQfspshc'
def save_chart():
  res = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1')
  prices_res = res.json().get('prices')
  for price in prices_res:
    dt_object = datetime.utcfromtimestamp(price[0]/1000)
    price[0] = dt_object.strftime("%H:%M:%S")
    
  df = pd.DataFrame(dict(
    time=[i[0] for i in prices_res],
    price=[i[1] for i in prices_res],
  ))
  if not os.path.exists(r'C:\Users\KIIT\Desktop\bitcoin_tracker\images'):
    os.mkdir(r'C:\Users\KIIT\Desktop\bitcoin_tracker\images')
  with Image.open(r'C:\Users\KIIT\Desktop\bitcoin_tracker\images\background.jpg') as bg_image:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['time'], y=df['price'], line=dict(width=6), mode='lines'))
    fig.update_layout(
      plot_bgcolor='#141721',
      yaxis_title='Price',
      xaxis_title='Last 24h',
      xaxis_showgrid=False,
      xaxis_showticklabels=False,
      yaxis_gridcolor='#2f4a66',
      yaxis_tickformat = '.12f',
      yaxis_linecolor='#4a89ff',
      height=512,
      width=1052,
      margin=dict(r=0, l=10, b=10, t=0),
      font=dict(size=24)
    )
    fig.add_layout_image(
      dict(
         source=bg_image,
        xref="paper",
        yref="paper",
        x=0,
        y=1,
        sizex=1,
        sizey=1,
        sizing="stretch",
        opacity=0.3,
        layer="below")
     )
    fig.write_image(r'C:\Users\KIIT\Desktop\bitcoin_tracker\images\fig1.png')   

def btcchart(update, context):
   chat_id = update.effective_chat.id
   save_chart()
   context.bot.send_photo(chat_id, photo=open(r'C:\Users\KIIT\Desktop\bitcoin_tracker\images\fig1.png', 'rb'))
updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher
#---------------------/btcchart---------------------
dispatcher.add_handler(CommandHandler("btcchart", btcchart))
dispatcher.add_handler(CommandHandler("dynamiccsv",dynamiccsv ))
dispatcher.add_handler(CommandHandler("feedback", feedback))
dispatcher.add_handler(CommandHandler("qr",qr))
dispatcher.add_handler(CommandHandler("version", version))
dispatcher.add_handler(CommandHandler("forecast", forecast))
dispatcher.add_handler(CommandHandler("csv", csv))
dispatcher.add_handler(CommandHandler("portfolio", portfolio))
updater.start_polling()
