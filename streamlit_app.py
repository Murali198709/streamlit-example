
import requests
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
from sklearn import tree
import streamlit as st
import matplotlib.pyplot as plt





st.title("Murali Krishna Tulluri's Data mining course Assignment 6")


values = st.slider('Please select a range of values',1,365, (15, 150))


Currency = st.radio(

    "Currency",

    ('CAD','USD','INR'))


url="https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency="+Currency+"&days="+str(values[1])+"&interval=daily.json"

JSONContent = requests.get(url).json()


bitcoin_prices = pd.DataFrame(JSONContent['prices'],columns=['date',Currency])

bitcoin_prices['date'] = pd.to_datetime(bitcoin_prices['date'],unit='ms')

start_date = bitcoin_prices['date'].min()+timedelta(days=values[0])

bitcoin_prices = bitcoin_prices[bitcoin_prices['date']>=start_date]

bitcoin_prices = bitcoin_prices.set_index('date')


st.line_chart(bitcoin_prices[Currency])
st.write('Average price during this period was '+str(bitcoin_prices[Currency].mean())+Currency)
    

   
