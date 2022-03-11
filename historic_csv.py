
 




import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

def historiccsv():
    history = yf.download(tickers='BTC-USD', period = 'MAX', interval = '1d')
    history.to_csv(r'C:\Users\KIIT\Desktop\bitcoin_tracker\BTC-USD.csv')

historiccsv()

   
