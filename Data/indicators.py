class simple_moving_average(object):
    def __init__(self, minutes):
        self.minutes = minutes
        self.memory = [0] * minutes
        self.ma = 0
    
    def update_ma(self, price):
        self.ma -= self.memory[0]/self.minutes
        self.ma += price/self.minutes

        self.memory.pop(0)
        self.memory.append(price)

# class indicator(object):
#     def __init__(self):
#         return