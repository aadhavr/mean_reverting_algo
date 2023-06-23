import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

yf.pdr_override()

input_symbol = input('Enter stock ticker: ')
input_mean_frame = input('Enter time frame for mean: ')  # time frame for calculating the mean
input_backtest_frame = input('Enter time frame for backtest: ')  # time frame for the backtest

def mean_reversion_strategy(symbol, mean_frame, backtest_frame):
    start_date = '2018-08-01' # modify this to your liking
    end_date = '2023-06-23'
    stock_data = pd.DataFrame(yf.download(symbol, start=start_date, end=end_date)['Close'])

    # the window is the mean_frame to avoid using redundant data
    mean_data = stock_data['Close'].rolling(window=mean_frame).mean()

    # calculates z scores
    stock_data['returns'] = stock_data['Close'].pct_change()
    stock_data['z_score'] = (stock_data['Close'] - mean_data) / stock_data['Close'].rolling(window=mean_frame).std()

    # figures out entry and exit thresholds
    percentiles = [5, 10, 50, 90, 95]
    z_scores = stock_data['z_score'].dropna()
    percentile_values = np.percentile(z_scores, percentiles)


    buy = percentile_values[1] # z-score threshold for entry signal
    sell = percentile_values[3]  # z-score threshold for exit signal                                         
    stock_data['Signal'] = np.where(stock_data['z_score'] > sell, -1, np.where(stock_data['z_score'] < buy, 1, 0))

    backtest_data = stock_data[-backtest_frame:]
    backtest_data['Signal'] = backtest_data['Signal'].shift(1)  # shifts signals by one day
    backtest_data['StrategyReturn'] = backtest_data['Signal'] * backtest_data['returns']
    backtest_data['CumulativeReturn'] = (1 + backtest_data['StrategyReturn']).cumprod()

    plt.plot(np.exp(backtest_data['returns'].dropna()).cumprod(), label = "buy, hold")
    plt.plot(np.exp(backtest_data['StrategyReturn'].dropna()).cumprod(), label = "strategy")
    plt.xlabel('Date')
    plt.ylabel('Returns')
    plt.legend()
    plt.show()


mean_reversion_strategy(input_symbol, int(input_mean_frame), int(input_backtest_frame))