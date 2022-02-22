import data 
import indicators

simple_moving_average_3 = indicators.simple_moving_average(3)
async def tsla_handler(bar):
    print(bar)
    simple_moving_average_3.update_ma(bar.close)


tsla = data.data_ticker_bars('TSLA', tsla_handler)
tsla.start()

class algotrading(object):
    def __init__(self):
        pass

    # def cross(self):