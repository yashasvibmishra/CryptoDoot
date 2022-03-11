#!/usr/bin/env python
# coding: utf-8

# In[2]:



 



import pandas as pd
from fbprophet import Prophet
import plotly.graph_objects as go
import pandas_datareader as web
from datetime import datetime
from datetime import timedelta


# In[3]:


df = pd.read_csv('BTC-USD.csv')
df = df[["Date", "Close"]]
df.columns = ["ds", "y"]
print(df)


# In[4]:


prophet = Prophet(seasonality_mode="multiplicative")
prophet.fit(df)


# In[5]:


future = prophet.make_future_dataframe(periods=365)
print(future)


# In[6]:


forecast = prophet.predict(future)
forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(200)


# In[7]:


from fbprophet.plot import plot
prophet.plot(forecast, figsize=(15, 10))


# In[8]:


prophet.plot(forecast).savefig('1.png')


# In[10]:


today = datetime.today().strftime('%Y-%m-%d')
next_day = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
forecast[forecast['ds'] == next_day]['yhat'].item()

