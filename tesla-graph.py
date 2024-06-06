import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# Define the stock symbol for Tesla
symbol = 'TSLA'

# Fetch the stock data
stock_data = yf.Ticker(symbol)

# Get financial data
income_statement = stock_data.financials
balance_sheet = stock_data.balance_sheet
cash_flow = stock_data.cashflow

# Transpose the data for easier plotting
income_statement = income_statement.T
balance_sheet = balance_sheet.T
cash_flow = cash_flow.T

# Plotting the data
plt.figure(figsize=(14, 7))

# Plot revenue
plt.subplot(3, 1, 1)
plt.plot(income_statement.index, income_statement['Total Revenue'], marker='o')
plt.title('Tesla Financial Data')
plt.ylabel('Total Revenue')
