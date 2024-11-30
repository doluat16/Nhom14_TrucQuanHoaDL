import yfinance as yf
import pandas as pd

# Lấy thông tin cơ bản của một mã cổ phiếu
ticker_symbol = "AAPL"  # Ví dụ: mã cổ phiếu Apple
stock = yf.Ticker(ticker_symbol)

data = stock.history(period = '5y')

data.to_csv('stocks.csv')
print('Done!!!')