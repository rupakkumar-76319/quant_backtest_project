# Quantitative Research Project: Moving Average Backtesting

## 📘 Overview
This project implements a **Moving Average Crossover Strategy** for stock trading.
It backtests historical stock data (e.g., Apple - AAPL) using Python to evaluate
profitability, Sharpe ratio, and drawdown.

## ⚙️ Features
- Load and clean historical data
- Select custom date ranges
- Build short-term and long-term moving average crossover strategy
- Calculate returns, Sharpe Ratio, and Max Drawdown
- Plot performance with buy/sell signals
- Save result summary and performance chart automatically

## 📊 Project Structure
quant_backtest_project/
├── Data/ # CSV files (e.g., AAPL.csv)
├── output/ # Saved plots and reports
├── src/
│ ├── utils.py
│ ├── strategy.py
│ ├── backtest.py
│ ├── visualization.py
│ └── main.py
├── LICENSE
├── README.md
└── requirements.txt

## 🛠️ How to Run
1. Clone the repo or download the folder.
2. Install dependencies:
   In terminal(vs code default) bash
    pip install -r requirements.txt
    python main.py

## Output
Results (performance summary & plots) are saved in the `output/` folder.

🧑‍💻 Author
Rupak Kumar
