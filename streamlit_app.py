
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

#bitcoin_prices.plot.line(x="date",y="price")

Currency = st.radio(

    "Currency",

    ('CAD','USD','INR'))



#specifying what should be display when the radio button is selected

if Currency == 'CAD':

    st.write('You select Canada')

elif Currency == 'USD':

    st.write("You selected USD.")
else:

    st.write("You INR")