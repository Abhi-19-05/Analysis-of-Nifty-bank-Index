import yfinance as yf
from datetime import date
import datetime
import pandas as pd

# Define the list of bank stocks
stocks = [
    "^NSEBANK", "AUBANK.NS", "AXISBANK.NS", "BANKBARODA.NS", "CANBK.NS",
    "FEDERALBNK.NS", "HDFCBANK.NS", "ICICIBANK.NS", "IDFCFIRSTB.NS",
    "INDUSINDBK.NS", "KOTAKBANK.NS", "PNB.NS", "SBIN.NS"
]

# Set start and end dates for stock data (last 365 days)
start_date = datetime.datetime.now() - datetime.timedelta(days=365)
today_date = date.today()

# Initialize an empty dataset
dataset = None

# Fetch data for each stock and append to the dataset
for index, stock in enumerate(stocks):
    temp = yf.download(stock, start=start_date, end=today_date)
    temp["Date"] = temp.index
    temp["Symbol"] = stock  # Renamed 'Stock' column to 'Symbol' directly here

    if index == 0:
        print("1")  # Debug print to indicate first stock data fetch
        dataset = temp
    else:
        print("2")  # Debug print to indicate subsequent stock data fetches
        dataset = dataset._append(temp)

del temp  # Clean up temporary variable

print(dataset.head())
