from alpaca_trade_api.stream import Stream
import credentials

# Getting data in bars each minute
class data_ticker_bars(object):
    def __init__(self, ticker, handler):
        self.handler = handler
        self.ticker = ticker
        self.stream = 0
    
    def start(self):
        # Initiate Class Instance
        self.stream = Stream(credentials.APCA_API_KEY_ID, credentials.APCA_API_SECRET_KEY, base_url=credentials.APCA_API_BASE_URL, data_feed='iex')

        # Subscribing to event
        self.stream.subscribe_bars(self.handler, str(self.ticker))

        self.stream.run()

# Getting data from each trade made 
class data_ticker_trades(object):
    def __init__(self):
        pass