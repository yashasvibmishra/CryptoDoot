# Copyright (C) Yashasvi Baneswar Mishra - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Yashasvi Baneswar Mishra <yashasvimishra1@gmail.com>, March 2022
 


import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_prices

telegram_bot_token = '5101284223:AAGuasvtgsxtypb9n4Eu8Kk7soGqQfspshc'

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
    message = "sending the csv file"
    context.bot.send_document(chat_id, document=open(r'C:\Users\KIIT\Desktop\bitcoin_tracker\BTC-USD.csv', 'rb'))

def forecast(update, context):
    chat_id = update.effective_chat.id
    message = "sending the forecast chart"
    context.bot.send_photo(chat_id, photo=open(r'C:\Users\KIIT\Desktop\bitcoin_tracker\1.png', 'rb'))

dispatcher.add_handler(CommandHandler("forecast", forecast))
dispatcher.add_handler(CommandHandler("csv", csv))
dispatcher.add_handler(CommandHandler("portfolio", portfolio))
updater.start_polling()