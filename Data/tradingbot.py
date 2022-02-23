import data 
import indicators
import alpaca_trade_api as tradeapi

# API to submit orders, etc... 
api = tradeapi.REST()

# Setting up indicators
#   macd
fast_ema = indicators.exponential_moving_average(12)
slow_ema = indicators.exponential_moving_average(26)
macd_standard = indicators.macd(fast_ema, slow_ema)

#   signal line
signal_line = indicators.exponential_moving_average(9)

#   long term trend
long_term_trend = indicators.exponential_moving_average(100)

# Algorithm for trading
async def bars_handler(bar):
    print(bar)

    # Updating averages 
    fast_ema.update_ema(bar.close)
    slow_ema.update_ema(bar.close)
    macd_standard.update_macd()
    signal_line.update_ema(macd_standard.macd)
    long_term_trend.update_ema(bar.close)

    # Uptrend
    if(bar.close >= long_term_trend.ema):
        # Check for buy opportunity
        # If bought, look for sell opportunity
        pass

    # Downtrend
    else:
        pass

tsla = data.data_ticker_bars('TSLA', bars_handler)
tsla.start()
