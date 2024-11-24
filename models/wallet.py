from models.cryptocurrency import Cryptocurrency
from users.trader import Trader


class Wallet:
    def __init__(self, trader: Trader):
        self.trader = trader
        self.__cryptos = {}  # Private attribute, holds cryptocurrencies

    def add_crypto(self, cryptocurrency, amount):
        if not isinstance(cryptocurrency, Cryptocurrency):
            raise ValueError("Invalid cryptocurrency.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")

        if cryptocurrency.symbol in self.__cryptos:
            self.__cryptos[cryptocurrency.symbol]["amount"] += amount
        else:
            self.__cryptos[cryptocurrency.symbol] = {"crypto": cryptocurrency, "amount": amount}
        print(f"Added {amount} units of {cryptocurrency.name} to the wallet.")

    def view_wallet(self):
        print("Wallet Contents:")
        for symbol, data in self.__cryptos.items():
            print(f"{data['crypto']} - Amount: {data['amount']}")
