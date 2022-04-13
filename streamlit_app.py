
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn import tree
import streamlit as st


url='https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=cad&days=90&interval=daily.json'

JSONContent = requests.get(url).json()


bitcoin_prices = pd.DataFrame(JSONContent['prices'],columns=['date','price'])


#print(bitcoin_prices.count())

bitcoin_prices['date'] = pd.to_datetime(bitcoin_prices['date'],unit='ms')


st.title("Murali Krishna Tulluri's Data mining course Assignment 6")

bitcoin_prices['date'] = pd.to_datetime(bitcoin_prices['date']).dt.date

Count = bitcoin_prices["date"].nunique()


values = st.slider(
     'Select number of days you want to see the Bitcoin price trend and average price',
     1, int(Count), (1, 15))
st.write('Values:', values)

Currency = st.radio(

    "Currency",

    ('CAD','USD','INR'))

bitcoin_prices['CAD_price'] = bitcoin_prices["price"]*1.26
bitcoin_prices['INR_price'] = bitcoin_prices["price"]*76.12

#specifying what should be display when the radio button is selected

if Currency == 'CAD':
        
    
    bitcoin_prices.plot.line(x="date",y="price",label="CAD")
    st.write('Average price during this period was '+str(bitcoin_prices['CAD_price'].mean()))
    

elif Currency == 'USD':

    bitcoin_prices.plot.line(x="date",y="price",label="USD")
    st.write('Average price during this period was '+str(bitcoin_prices['price'].mean()))
else:

    bitcoin_prices.plot.line(x="date",y="price",label="INR")
    st.write('Average price during this period was '+str(bitcoin_prices['INR_price'].mean()))
    
