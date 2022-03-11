
 




import requests
res = requests.get('https://api.coingecko.com/api/v3/coins/lunadoge/market_chart?vs_currency=usd&days=1')
prices_res = res.json().get('prices')

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
telegram_bot_token = '5101284223:AAGuasvtgsxtypb9n4Eu8Kk7soGqQfspshc'
def save_chart():
   pass


def save_chart():
  res = requests.get('https://api.coingecko.com/api/v3/coins/lunadoge/market_chart?vs_currency=usd&days=1')
  prices_res = res.json().get('prices')
  for price in prices_res:
    dt_object = datetime.utcfromtimestamp(price[0]/1000)
    price[0] = dt_object.strftime("%H:%M:%S")
    
  df = pd.DataFrame(dict(
    time=[i[0] for i in prices_res],
    price=[i[1] for i in prices_res],
  ))
  if not os.path.exists("images"):
    os.mkdir("images")
  with Image.open("images/background.jpg") as bg_image:
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
    fig.write_image("images/fig1.png")

    dt_object = datetime.utcfromtimestamp(price[0]/1000)
    price[0] = dt_object.strftime("%H:%M:%S")   

    fig.write_image("images/fig1.png")

def chart(update, context):
   chat_id = update.effective_chat.id
   save_chart()
   context.bot.send_photo(chat_id, photo=open('images/fig1.png', 'rb'))
updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher
# The chart function will be called when someone types /chart
dispatcher.add_handler(CommandHandler("chart", chart))
# Start listening for chat commands
updater.start_polling()
