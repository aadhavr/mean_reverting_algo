import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

yf.pdr_override()

symbol = "AAPL"
mean_frame = 21  # Time frame for calculating the mean
backtest_frame = 90  # Time frame for the backtest

start_date = '2018-08-01'
end_date = '2022-12-31'
stock_data = pd.DataFrame(yf.download(symbol, start=start_date, end=end_date)['Close'])

# Calculate the mean for the mean-reversion strategy
mean_data = stock_data['Close'].rolling(window=mean_frame).mean()

# Calculate the returns and z-scores
stock_data['returns'] = stock_data['Close'].pct_change()
stock_data['z_score'] = (stock_data['Close'] - mean_data) / stock_data['Close'].rolling(window=mean_frame).std()

# Figure out entry and exit thresholds
percentiles = [5, 10, 50, 90, 95]
z_scores = stock_data['z_score'].dropna()
percentile_values = np.percentile(z_scores, percentiles)


buy = percentile_values[1] # Z-score threshold for entry signal
sell = percentile_values[3]  # Z-score threshold for exit signal                                         
stock_data['Signal'] = np.where(stock_data['z_score'] > sell, -1, np.where(stock_data['z_score'] < buy, 1, 0))

backtest_data = stock_data[-backtest_frame:]
backtest_data['Signal'] = backtest_data['Signal'].shift(1)  # Shift the signals by one day
backtest_data['StrategyReturn'] = backtest_data['Signal'] * backtest_data['returns']
backtest_data['CumulativeReturn'] = (1 + backtest_data['StrategyReturn']).cumprod()

plt.plot(np.exp(backtest_data['returns'].dropna()).cumprod(), label = "buy, hold")
plt.plot(np.exp(backtest_data['StrategyReturn'].dropna()).cumprod(), label = "strategy")
plt.xlabel('Date')
plt.ylabel('Returns')
plt.legend()
plt.show()