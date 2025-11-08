from src.utils import load_data, prepare_data
from src.strategy import moving_avg_strategy
from src.backtest import run_backtesting
from src.visualization import plot_result
from datetime import datetime

'Step-1'
data=load_data("Data/AAPL.csv")

'Step-2'
data= prepare_data(data)

'step-3'
starting_date=input("Enter the starting date(YYYY-MM-DD) : ")
ending_date=input("Enter the ending date(YYYY-MM-DD) : ")
my_Pattern="%Y-%m-%d"
starting_date_object= datetime.strptime(starting_date, my_Pattern)
ending_date_object= datetime.strptime(ending_date, my_Pattern)
data = data[(data['Date'] >= starting_date_object) & (data['Date'] <= ending_date_object)]
print(f"\nData filtered from {starting_date_object.date()} to {ending_date_object.date()}")

'Step-4'
short_term = int(input("Enter short-term moving average window: "))
long_term = int(input("Enter long-term moving average window: "))
data = moving_avg_strategy(data, short_term, long_term)

'Step-5'
moneyYouHave = int(input("Enter the amount of money do u want to invest in it : $"))
data, sharpe_ratio, max_drawdown, percent_return = run_backtesting(data, moneyYouHave)

'step-6'
plot_result(data, sharpe_ratio, max_drawdown, percent_return)
print(data['Signal_Change'].value_counts())