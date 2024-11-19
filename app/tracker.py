import time
import ccxt
from app.exchange import Exchange
from app.notifications import Notification

class PriceTracker:
    def __init__(self, exchange, symbol, buy_price, sell_price):
        self.exchange = exchange
        self.symbol = symbol
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.exchange_obj = Exchange(exchange)
        self.prev_price = None
        self.notification = Notification()

    def fetch_ticker(self):
        return self.exchange_obj.fetch_ticker(self.symbol)['last']

    def check_price_thresholds(self, price):
        if price == self.buy_price:
            self.notification.trigger_buy_notification()
        elif price == self.sell_price:
            self.notification.trigger_sell_notification()

    def start_tracking(self):
        while True:
            try:
                price = self.fetch_ticker()

                if price != self.prev_price:
                    print(price)
                    self.prev_price = price

                self.check_price_thresholds(price)
                time.sleep(1)

            except Exception as e:
                print(f"Error getting price updates for {self.exchange} - {self.symbol}: {e}")
                time.sleep(10)
