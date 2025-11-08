def moving_avg_strategy(data, short_window, long_window):
    data['SMA_Short']= data['Adj Close'].rolling(window=short_window).mean()
    data['SMA_Long']= data['Adj Close'].rolling(window=long_window).mean()

    data['Signal']=0

    data.loc[data['SMA_Short']> data['SMA_Long'], 'Signal']= 1
    print(f"✅ Strategy signals created successfully! (Short={short_window}, Long={long_window})")
    return data