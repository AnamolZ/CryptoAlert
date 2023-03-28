import ccxt
import requests
import time
from win10toast import ToastNotifier


def get_price_update(exchange, symbol, buy_price, sell_price):
    """Get real-time price updates for a given trading pair on a given exchange.

    Args:
        exchange (str): Name of the exchange (e.g. 'binance', 'kraken', etc.).
        symbol (str): Trading pair symbol (e.g. 'SOL/USDT', 'BTC/USD', etc.).
        buy_price (float): Buy price threshold for triggering a notification.
        sell_price (float): Sell price threshold for triggering a notification.

    Returns:
        None
    """

    exchange_obj = getattr(ccxt, exchange)()
    prev_price = None

    while True:
        try:
            ticker = exchange_obj.fetch_ticker(symbol)
            price = ticker['last']

            if price != prev_price:
                print(price)
                prev_price = price

            if price == buy_price:
                toaster = ToastNotifier()
                toaster.show_toast(f"{exchange.capitalize()}", "Buy Point Alert!", duration=10)

            if price == sell_price:
                toaster = ToastNotifier()
                toaster.show_toast(f"{exchange.capitalize()}", "Sell Point Alert!", duration=10)

            time.sleep(1)

        except (ccxt.ExchangeError, ccxt.NetworkError, requests.RequestException) as e:
            print(f"Error getting price updates for {exchange} - {symbol}: {e}")
            time.sleep(10)


def main():
    exchanges = ['binance']  # Add more exchanges here if needed
    symbols = ['SOL/USDT']  # Add more trading pairs here if needed
    buy_price = 18.70
    sell_price = 21.02

    for exchange in exchanges:
        for symbol in symbols:
            get_price_update(exchange, symbol, buy_price, sell_price)


if __name__ == '__main__':
    main()
