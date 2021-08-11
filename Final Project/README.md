## Backtesting Platform for Algorithmic Trading with Technical Indicators

This tool is designed to backtest different trading strategies in order to choose the best strategies with the best parameters for the highest profitability. The user can choose to automate the strategy and parameter search or conduct tests manually. The data is pulled directly from Oanda via the Python Quants API.

![backtester_demo_1](backtester_demo_1.gif)

The tool currently supports a selection of instruments with a granularity of daily candles within a selectable time frame. It shows the total gain or loss of the strategy and compares this to a 'buy and hold' strategy. Both 'buy and hold' (blue) as well as the custom strategy's cumulative returns (orange) are shown in ineractive graphs.

![backtester_demo_2](backtester_demo_2.gif)

The Backtesting scripts are based on the contents of Prof. Alexander Hagemanns scripts in the Algorithmic Trading course.

Current features at a glance:

- Instruments:
    - EUR/US
    - BTC/US
    - S&P 500
    - EUR/AUD
    - USD/HKD
  
  
- Custom time frame within the last 5 years
- Strategies:
    - Simple Moving Averages
    - Mean Reversion (Bollinger Bands)
    - Logistic Regression
    - Combining of the above Strategies
        - by tendency
        - by unanimous indication
- Optimization with scipy brute algorithm

Technologies used:

- Python
- Scipy Package
- The Python Quants API
- Streamlit

Features planned for future versions:

- more instruments
- more granularity options
- more methods of combination
- more efficient optimization algorithms
- SQL Database for faster data collection

Installation Guide

1. Clone the repository 
2. Pip install everything from the requirements.txt
3. Run the web app in your browser with:

streamlit run forex_backtester_app.py
