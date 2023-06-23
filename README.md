# Mean Reversion Strate

![image](https://github.com/aadhavr/mean_reverting_algo/assets/32024444/0edfae4c-a545-4c75-931b-b8213e7e8fd7)



This script implements a mean reversion strategy for a given stock. It calculates the z-scores for the stock's price and generates entry and exit signals based on predefined thresholds. The script also performs a backtest on the strategy and visualizes the returns.

## Disclaimer

Please note that the information provided by this script is for educational and informational purposes only. It should not be considered as financial or investment advice. The strategy implemented in this script may not be suitable for all investors. Investing in the stock market carries inherent risks, and past performance is not indicative of future results. Before making any investment decisions, it is recommended to consult with a qualified financial advisor.

## Prerequisites

Before running this script, ensure that you have the following dependencies installed:

- pandas
- numpy
- yfinance
- matplotlib
- pandas_datareader

You can install the dependencies using the following command:
'''
pip install pandas numpy yfinance matplotlib pandas_datareader
'''

## Usage

1. Clone or download the repository to your local machine.

2. Install the required Python libraries mentioned in the prerequisites section.

3. Open the `backtesting_mean_revert.py` file in a text editor.

4. As you see fit, make changes to the thresholds, time frame for the mean calculation, and time frame for the backtesting. (Note: there is a distinct difference in these timeframes to intentionally avoid lookahead bias)

5. Run the `backtesting_mean_revert.py` script using the following command:
    
```
python3 backtesting_mean_revert.py
```
6. You will be prompted to enter the stock ticker, time frame for mean calculation, and time frame for backtesting.

7. A graph showing both strategies will be created.

## Note on Lookahead Bias

This script aims to simulate a mean reversion strategy based on historical data while mitigating the risk of lookahead bias. Lookahead bias is a common pitfall in backtesting, where future information is unintentionally incorporated into the development or evaluation of a trading strategy, leading to overly optimistic or unrealistic results.

To address lookahead bias, this script employs the following measures:

   -  Mean Calculation: The mean of the stock's closing prices is calculated using a specific time frame, as provided by the user. This mean calculation is done using historical data up until the given end date, without incorporating any future information. By using historical data, the script aims to capture the underlying trend within the specified time frame.

   -  Backtesting: The backtesting of the strategy is performed using a different time frame, also specified by the user. This separation of time frames ensures that the strategy is evaluated based on historical data that is independent of the mean calculation period. The backtesting is conducted using data starting from the end of the mean calculation period until the end date, thus avoiding the use of future information during the testing phase.

By utilizing distinct time frames for mean calculation and backtesting, this script attempts to mitigate the risk of lookahead bias and provide a more realistic assessment of the strategy's performance.
