import pandas as pd 
import numpy as np

def run_backtesting(data, moneyYouHave):
    """
    Backtest the moving average strategy:
    - Uses the 'Signal' column to decide when to be in or out of the market.
    - Calculates profit, final balance, and return %.
    """

    '''
    These backtesting divides into four major parts. And these are the backbone of the backtest.
    - Daily percentage change in stock price.
    - Strategy return.
    - Growth of $1 over time (cumulative product of returns).
    - Final portfolio value.
    let's build with the help of these four.
    '''

    'Step-1'
    data['daily_return']= data['Close'].pct_change()

    'step-2'
    data['Strategy_return']= data['daily_return'] * data['Signal'].shift(1)

    'step-3'
    data['Cumulative_market'] = (1 + data['daily_return']).cumprod()
    data['Cumulative_strategy'] = (1 + data['Strategy_return']).cumprod()

    'step-4'
    final_strategy = moneyYouHave * data['Cumulative_strategy'].iloc[-1]
    final_market = moneyYouHave * data['Cumulative_market'].iloc[-1]
    profit = final_strategy - moneyYouHave
    percent_return = ((final_strategy / moneyYouHave) - 1) * 100

    strategy_returns = data['Strategy_return'].dropna()
    sharpe_ratio = (strategy_returns.mean() / strategy_returns.std()) * np.sqrt(252)

    strategy_returns = data['Strategy_return'].dropna()
    sharpe_ratio = (strategy_returns.mean() / strategy_returns.std()) * np.sqrt(252)
    cumulative = (1 + strategy_returns).cumprod()
    rolling_max = cumulative.cummax()
    drawdown = (cumulative - rolling_max) / rolling_max
    max_drawdown = drawdown.min()

    summary_text = (
    "PERFORMANCE SUMMARY\n"
    + "-" * 40 + "\n"
    + f"Initial Investment : ${moneyYouHave:,.2f}\n"
    + f"Final Market Value : ${final_market:,.2f}\n"
    + f"Final Strategy Value : ${final_strategy:,.2f}\n"
    + f"Total Profit : ${profit:,.2f} ({percent_return:.2f}%)\n"
    + f"Sharpe Ratio : {sharpe_ratio:.2f}\n"
    + f"Max Drawdown : {max_drawdown:.2f}%\n"
    )

    print(summary_text)

    with open("Output/summary/strategy_performance.txt", "w") as f:
        f.write(summary_text)

    return data, sharpe_ratio, max_drawdown, percent_return