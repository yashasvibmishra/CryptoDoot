# Copyright (C) Yashasvi Baneswar Mishra - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Yashasvi Baneswar Mishra <yashasvimishra1@gmail.com>, March 2022
 




import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

def historiccsv():
    history = yf.download(tickers='BTC-USD', period = 'MAX', interval = '1d')
    history.to_csv(r'C:\Users\KIIT\Desktop\bitcoin_tracker\BTC-USD.csv')

historiccsv()

   