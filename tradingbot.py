import data 
import indicators
import alpaca_trade_api as tradeapi

# API to submit orders, etc... 
api = tradeapi.REST()

ticker_symbol = 'TSLA'

# Setting up indicators
#   macd
fast_ema = indicators.exponential_moving_average(12)
slow_ema = indicators.exponential_moving_average(26)
macd = indicators.macd(fast_ema, slow_ema)

#   signal line
signal_line = indicators.exponential_moving_average(9)

#   long term trend
long_term_trend = indicators.exponential_moving_average(100)

#   swing low
swing_low = indicators.swing_low()

# Algorithm for trading
bought = False  
async def bars_handler(bar):
    print(bar)
 
    # Updating averages 
    fast_ema.update_ema(bar.close)
    slow_ema.update_ema(bar.close)
    macd.update_macd()
    signal_line.update_ema(macd.macd)
    long_term_trend.update_ema(bar.close)
    swing_low.update_swing_low(bar.low)

    # Check for selling opportunity
    if(bought):
        # Check for crossunder
        if(macd.memory[0] >= signal_line.memory[0] and macd.memory[1] <= signal_line.memory[1]):
            if(api.get_position(ticker_symbol).qty > 0):
                api.cancel_all_orders()
                api.submit_order(ticker_symbol, 1, 'sell', 'market', 'day')
                bought = False
        return

    # Uptrend
    if(bar.close >= long_term_trend.ema):
        # Check for buy opportunity
        if(macd.memory[0] <= signal_line.memory[0] and macd.memory[1] >= signal_line.memory[1]):
            bought = True
            api.submit_order(ticker_symbol, 1, 'buy', 'market', 'day')
            api.submit_order(ticker_symbol, 1, 'sell', 'limit', 'day', stop_loss={"stop_price": str(swing_low.swing_low), "limit_price": str(1.5 * swing_low.swing_low)})

    

tsla = data.data_ticker_bars('TSLA', bars_handler)
tsla.start()
