import matplotlib.pyplot as plt
import os

def plot_result(data, sharpe_ratio, max_drawdown, percent_return):

    """
    Plots:
    1. Stock price with short & long moving averages
    2. Cumulative Market vs Strategy performance
    """

    plt.figure(figsize=(12,6))

    # --- Plot 1: Price and Moving Averages ---
    plt.subplot(2,1,1)
    plt.plot(data['Date'], data['Adj Close'], label='Price', alpha=0.7)
    plt.plot(data['Date'], data['SMA_Short'], label='Short MA', linestyle='--')
    plt.plot(data['Date'], data['SMA_Long'], label='Long MA', linestyle='--')

    # Marking buy and sell singnal
    data['Signal_Change'] = data['Signal'].diff()
    buy_signals=data[data['Signal_Change']==1]
    sell_signals=data[data['Signal_Change']==-1]

    plt.scatter(buy_signals['Date'], buy_signals['Adj Close'],
                marker='^', color='green', label='Buy Signal', s=80)
    plt.scatter(sell_signals['Date'], sell_signals['Adj Close'],
                marker='v', color='red', label='Sell Signal', s=80)


    plt.title('Stock Price with Moving Averages')
    plt.legend()
    plt.grid(True)

    # --- Plot 2: Strategy vs Market ---
    plt.subplot(2,1,2)
    plt.plot(data['Date'], data['Cumulative_market'], label='Market (Buy & Hold)')
    plt.plot(data['Date'], data['Cumulative_strategy'], label='Your Strategy')
    plt.title('Performance Comparison')
    plt.legend()
    plt.grid(True)

    metrics_text = f"Sharpe: {sharpe_ratio:.2f}\nDrawdown: {max_drawdown:.2f}%\nProfit: {percent_return:.2f}%"
    plt.gcf().text(0.78, 0.25, metrics_text, fontsize=10,
               bbox=dict(facecolor='white', edgecolor='black'))

    plt.tight_layout()
    os.makedirs("Output/figures", exist_ok=True)

    plt.savefig("Output/figures/strategy_performance.png", dpi=300, bbox_inches='tight')
    plt.show()
    return data, sharpe_ratio, max_drawdown, percent_return