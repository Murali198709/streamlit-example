
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn import tree
import streamlit as st


"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""





url='https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=cad&days=90&interval=daily.json'

JSONContent = requests.get(url).json()


bitcoin_prices = pd.DataFrame(JSONContent['prices'],columns=['date','price'])


#print(bitcoin_prices.count())

bitcoin_prices['date'] = pd.to_datetime(bitcoin_prices['date'],unit='ms')


st.title("Murali Krishna Tulluri's Data mining course Assignment 6")

bitcoin_prices.plot.line(x="date",y="price")

