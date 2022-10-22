import yfinance as yf
import streamlit as st
import pandas as pd

st.write('''
# Simple Stock Price

Show are the **stock price** end ***volume*** of Google!

''')

# define the ticker simbol
tickerSimbol = 'GOOGL'

#get a data on this ticker
tickerData = yf.Ticker(tickerSimbol)

#get the historical price for this ticker
tickerDf = tickerData.history(period='1d', start='2010-05-31', end='2022-10-21')

#open high low close volume  dividends stock price  
st.write("## **Closing Price**")
st.line_chart(tickerDf.Close)
st.write("## **Volume Price**")
st.line_chart(tickerDf.Volume)


hide_st_style = '''
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
'''
st.markdown(hide_st_style, unsafe_allow_html=True)