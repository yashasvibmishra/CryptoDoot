# CryptoDoot

# Copyright (C) Yashasvi Baneswar Mishra - All Rights Reserved
# Blatant plagirsm of this file, via any medium is strictly prohibited
# Written by Yashasvi Baneswar Mishra <yashasvimishra1@gmail.com>, March 2022






INTRODUCTION

What is the project about?
[ Link: https://t.me/CryptoDootBot  ]
A Telegram bot that keeps track of the latest Cryptocurrency prices of Various Crypto-based coins and updates the user with the price fluctuations and helps in charting a course for future buyers. Try to think of it as your one-stop destination for when you think about navigating the uncharted waters of various exotic and new Cryptocurrencies. It aims to come with Graphs, Notification & Forecasting options as well, to aid the user in making better, reliable & informed decisions. 

Background:

These days, cryptocurrencies, notably 'Bitcoin,' are the trendiest topic. The problem is that the price of bitcoin is incredibly unpredictable, and you never know where it will be at the end of the day. Isn't it tough to keep track of the BTC price's continuous fluctuations?
Supply and demand, investor and user attitudes, government laws, and media frenzy all impact the price of Bitcoin. Price volatility is created by the interaction of all of these causes.
It's uncommon to watch cryptocurrency news without hearing an investor or fan's prediction for Bitcoin's price. Unfortunately, no one knows how high or low the price of cryptocurrencies will go.





Our Motivation behind this project:

For first-time investors, the cryptocurrency market is hardly a stroll in the park. It's crucial to have a good understanding of how the market works. It's important to remember that before picking an exchange, investors should check to see if the platform is sanctioned by regulations in their area. Everything should be taken into consideration, from the exchange giving access to certain cryptocurrencies to trading features – each and every component should be prioritised. It is not advisable to enter the mystical world of cryptocurrencies with the expectation of constantly being on the optimistic side. It is important to recognise that the cryptocurrency market is volatile and that the potential gains, as well as the possible losses, may be substantial. We wanted to change things for those looking to enter this magical realm of Crypto!
Being Crypto enthusiasts ourselves, we understood the effort that one had to put in to just keep a track of the fluctuating cryptocurrency prices.
So, we thought of building an end to end solution using python that would help us keep track of these prices through mobile notifications via the Telegram platform. And what better way to do that than using our very own custom proprietary bot!


Pivoting from, and building upon the initial reference idea:

Initially, we planned to build our crypto notification service using IFTTT and webhooks. (reference article:https://realpython.com/python-bitcoin-ifttt)
But, we found out that Coin Market Cap had updated their API which makes the process outdated.
So, we decided to move our notification service to a telegram by creating a telegram bot using python which would do the same job.
It is now that we realize, we are able to do much more using the telegram bot which wouldn't have been possible if we could have built the notification service using IFTTT. Live Plots, Forecasts, Coin 1 vs Coin 2 comparisons & much more! These all have been our biggest fortes, once we shifted to Telegram. 

PROJECT

Approach:

In this project, we created a Telegram bot that keeps track of the latest Cryptocurrency prices of various Crypto-based coins, notifies users of price swings, and assists future buyers in charting a course. 

For the goal of bitcoin price prediction using machine learning, several predictive algorithms have been researched and compared. In this project we used the Facebook Prophet model for Bitcoin price prediction using Python and machine learning.

The Facebook Prophet Library is an open-source additive regression model for time-series predictions made accessible by Facebook. While there is a more complex version of the Prophet, such as NeuralProphet, that is based on neural networks, for the Bitcoin price prediction challenge, We utilized the simpler version that employs machine learning techniques.





Requirements:
A coinmarketcap.com API key. Because we are going to make use of their API to get the latest bitcoin price.
The telegram app, and your account’s chat_id.
Then we are to make a  telegram bot using its own unique token key. Without the bot, one will not be able to send automated messages. In short, if you want to send price notifications from software to your telegram account, then you need a telegram bot.
 
 
Features and functions :

Bots are third-party applications that run inside Telegram. Users can interact with bots by sending them messages and commands. You control your bots using HTTPS requests to Telegram's Bot API.
The full API reference for developers is available here.
The functionalities that we added into our bot along with the commands that will be used to perform those functions are mentioned below:
 
 
 
1. Forecast:
Function: Shows the price for BTC in particular.
Command: /forecast

 
2. Live plots
Function/pricebot_get_single COIN_ID COIN_VS LAST_DAYS [SAME_MSG]: show chart and price information of the specified pair (single call)
COIN_NAME: CoinGecko ID
CURRENCY: CoinGecko CURRENCY short form
LAST_DAYS: The last number of days to show the price chart
SAME_MSG (optional): true for sending chart and price information in the same message (price information will be a caption of the chart image), false to send them in separate messages. Default value: true.: Shows chart and price information for the specified pair.
 



 
3. Get a CSV :
Function: Sends a CSV file to the user containing historic records of BTC over the past 8 years (up till the very day the command was sent).
Command: /csv


 
4. Check if the bot is working :
Function: This shows that the bot is alive, healthy & well, responding to user interactions. 
Command: /alive

 
5. About the bot :
Function: Shows CryptoDoot bot’s version information and credits.
Command: /version

6. View the world’s most diverse cryptocurrency portfolio
Function: displays the prices of an exotic bunch of Cryptocurrencies
Command: /portfolio

 
7. Generate a QR code
Function:  Fetch the official QR code for CryptoDoot. Share & Spread the word!
Command: /qr

 
8. Generate a dynamic CSV (unlike the static one earlier)
Function:  fetches a dynamic CSV file of Bitcoin priced in USD. It is for a 24 hour period, with a ticker set to 15 minutes.
Command: /dynamiccsv


 
9. We’d love to see your feedback!
Function:  Feel free to send us your valuable user feedback!
Command: /feedback
 

9. We’d love to see your feedback!
Process:

Getting Coinmarketcap API key
Bots are third-party applications that run inside Telegram. Users can interact with bots by sending the message
Telegram Bot and your chat id
Bots are third-party applications that run inside Telegram. Users can interact with bots by sending them commands and messages. 
Putting everything together
While there are a lot of things python scripts and programs can do on their own, one needs to extend their functionality and capabilities via various other libraries and packages. These 
 
 
CONCLUSION

What was accomplished /learned by the team during the project?


What would we (the team) have done differently, If we were doing this again for the first time?


What is our Future Outlook of CryptoDoot:- 


 
 
 
 
 
 
DISCLAIMER: 
Investing in cryptocurrencies and other Initial Coin Offerings ("ICOs") is very dangerous and speculative, and this report does not constitute a suggestion dossier by CryptoDoot to do so. Because each person's circumstance is different, one should always get advice from a knowledgeable finance specialist before making any financial decisions. 















