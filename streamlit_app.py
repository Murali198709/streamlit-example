
import requests
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
from sklearn import tree
import streamlit as st
import matplotlib.pyplot as plt

url='https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=cad&days=90&interval=daily.json'

JSONContent = requests.get(url).json()


bitcoin_prices = pd.DataFrame(JSONContent['prices'],columns=['date','price'])


#print(bitcoin_prices.count())

bitcoin_prices['date'] = pd.to_datetime(bitcoin_prices['date'],unit='ms')

Count = bitcoin_prices['date'].nunique()

st.title("Murali Krishna Tulluri's Data mining course Assignment 6")


min_date = bitcoin_prices['date'].min()

values = st.slider('Please select a range of values',1,91, (1, 70))
st.write('Values selected: ', values)
st.write(Count)
end_date = min_date + timedelta(days=int(values[1]))

bitcoin_prices=bitcoin_prices[bitcoin_prices['date']<=end_date]

Currency = st.radio(

    "Currency",

    ('CAD','USD','INR'))

bitcoin_prices['CAD'] = bitcoin_prices["price"]*1.26
bitcoin_prices['INR'] = bitcoin_prices["price"]*76.12
bitcoin_prices['USD'] = bitcoin_prices["price"]*1

bitcoin_prices = bitcoin_prices.set_index('date')

if Currency == 'CAD':
        

    
    st.line_chart(bitcoin_prices['CAD'])
    st.write('Average price during this period was '+str(bitcoin_prices['CAD'].mean())+' CAD')
    

elif Currency == 'USD':

    st.line_chart(bitcoin_prices['USD'])
    st.write('Average price during this period was '+str(bitcoin_prices['USD'].mean())+' USD')
else:

    st.line_chart(bitcoin_prices['INR'])
    st.write('Average price during this period was '+str(bitcoin_prices['INR'].mean())+' INR')


   
