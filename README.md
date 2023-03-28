# Trade Guard

Trade Guard is a Python program that monitors real-time price updates for a given trading pair on a specified exchange and triggers notifications when the price reaches a certain threshold. This program uses the ccxt library to fetch ticker data from supported exchanges and the win10toast library to display desktop notifications.

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies using pip:

    ```
    git clone https://github.com/AnamolZ/CryptoGuard.git
    pip install ccxt requests win10toast
    ```

## Usage

1. Open the command prompt or terminal.
2. Navigate to the directory where the `CryptoGuard.py` file is located.
3. Run the program by executing the following command:

    ```
    python CryptoGuard.py
    ```
4. The program will prompt you to enter the name of the exchange, trading pair symbol, buy price threshold, and sell price threshold.
5. Once you have entered the required information, the program will start monitoring price updates for the specified trading pair on the specified exchange.
6. When the price reaches the buy or sell threshold, a desktop notification will be displayed.

## Contributing

If you would like to contribute to Trade Alert, please fork the repository and submit a pull request. Suggestions, bug reports, and feature requests are also welcome. 

## License

This program is licensed under the [MIT License](https://github.com/example/trade-alert/blob/main/LICENSE).
