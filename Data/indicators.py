class simple_moving_average(object):
    def __init__(self, period):
        self.period = period
        self.memory = [0] * period
        self.sma = 0
    
    def update_sma(self, price):
        self.sma -= self.memory[0]/self.period
        self.sma += price/self.period

        self.memory.pop(0)
        self.memory.append(price)
        return self.sma

class exponential_moving_average(object):
    def __init__(self, period):
        self.period = period
        self.ema = 0
    
    def update_ema(self, price):
        k = 2 / (self.period + 1)
        old_ema = self.ema
        self.ema = price * k + old_ema * (1 - k)
        return self.ema

# Macd : short term momentum
class macd(object):
    def __init__(self, fast_ema, slow_ema):
        self.macd = 0
        self.fast_ema = fast_ema
        self.slow_ema = slow_ema

    # Standard: 12 EMA - 26 EMA
    def update_macd(self):
        self.macd = self.fast_ema - self.slow_ema
        return macd