import yfinance as yf
import pandas as pd
import matplotlib as mat
import numpy

amd=yf.Ticker("AMD")

#apple_share_price_data = apple.history(period='1d')
#apple_share_price_data.reset_index(inplace=True)
#apple.dividends.plot()

print(amd.info['country'])
print(amd.info['sector'])
df = amd.history(period="max")
print(type(df))
str= (df.head(1)['Volume'])
print(str)