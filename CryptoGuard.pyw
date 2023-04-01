import ccxt
import requests
import time
from win10toast import ToastNotifier
import pushbullet
from twilio.rest import Client


class PriceTracker:
    def __init__(self, exchange, symbol, buy_price, sell_price):
        self.exchange = exchange
        self.symbol = symbol
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.exchange_obj = getattr(ccxt, exchange)()
        self.prev_price = None
        self.pb = pushbullet.Pushbullet("ABCDEFGHIJKLMNOPQRST") # Add your pushbullet API key here
        self.account_sid = 'ABCDEFGHIJKLMNOPQRST' #  Add your twilio account sid here
        self.auth_token = 'ABCDEFGHIJKLMNOPQRST' # Add your twilio auth token here
        self.client = Client(self.account_sid, self.auth_token)

    def fetch_ticker(self):
        ticker = self.exchange_obj.fetch_ticker(self.symbol)
        return ticker['last']

    def check_price_thresholds(self, price):
        if price == self.buy_price:
            self.trigger_buy_notification()
        elif price == self.sell_price:
            self.trigger_sell_notification()

    def trigger_buy_notification(self):
        toaster = ToastNotifier()
        toaster.show_toast(f"{self.exchange.capitalize()}", "Buy Point Alert!", duration=10)
        self.pb.push_note("Buy Point Alert!", f"Price is at {self.buy_price}!")
        self.client.calls.create(url='http://demo.twilio.com/docs/voice.xml', to='+1234567890', # Add your number here
                                  from_='+1234567890') # Add twilio number here

    def trigger_sell_notification(self):
        toaster = ToastNotifier()
        toaster.show_toast(f"{self.exchange.capitalize()}", "Sell Point Alert!", duration=10)
        self.pb.push_note("Sell Point Alert!", f"Price is at {self.sell_price}!")
        self.client.calls.create(url='http://demo.twilio.com/docs/voice.xml', to='+1234567890', # Add your number here
                                  from_='+1234567890') # Add twilio number here

    def start_tracking(self):
        while True:
            try:
                price = self.fetch_ticker()

                if price != self.prev_price:
                    print(price)
                    self.prev_price = price

                self.check_price_thresholds(price)

                time.sleep(1)

            except (ccxt.ExchangeError, ccxt.NetworkError, requests.RequestException) as e:
                print(f"Error getting price updates for {self.exchange} - {self.symbol}: {e}")
                time.sleep(10)


def main():
    exchanges = ['binance']  # Add more exchanges here if needed
    symbols = ['SOL/USDT']  # Add more trading pairs here if needed
    buy_price = 18.01 # Add buy price here
    sell_price = 21.07 # Add sell price here

    trackers = []
    for exchange in exchanges:
        for symbol in symbols:
            tracker = PriceTracker(exchange, symbol, buy_price, sell_price)
            trackers.append(tracker)

    for tracker in trackers:
        tracker.start_tracking()


if __name__ == '__main__':
    main()
