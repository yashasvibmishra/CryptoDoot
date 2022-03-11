





# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go
def dynamic_csv():
    data = yf.download(tickers='BTC-USD', period = '24h', interval = '15m')
    print (data)

dynamic_csv()

