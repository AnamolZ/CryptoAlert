import ccxt

class Exchange:
    def __init__(self, exchange_name):
        self.exchange_name = exchange_name
        self.exchange_obj = getattr(ccxt, exchange_name)()

    def fetch_ticker(self, symbol):
        return self.exchange_obj.fetch_ticker(symbol)
