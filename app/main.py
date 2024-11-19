from app.tracker import PriceTracker
from app.config import EXCHANGES, SYMBOLS, BUY_PRICE, SELL_PRICE

def main():
    trackers = []
    for exchange in EXCHANGES:
        for symbol in SYMBOLS:
            tracker = PriceTracker(exchange, symbol, BUY_PRICE, SELL_PRICE)
            trackers.append(tracker)

    for tracker in trackers:
        tracker.start_tracking()

if __name__ == '__main__':
    main()
