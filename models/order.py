from users.trader import Trader
from models.cryptocurrency import Cryptocurrency


class Order:
    def __init__(self, trader: Trader, cryptocurrency: Cryptocurrency, amount, order_type):
        self.trader = trader
        self.cryptocurrency = cryptocurrency
        self.amount = amount
        self.order_type = order_type  # "BUY" or "SELL"

    def execute(self):
        print(f"Executing {self.order_type} order for {self.amount} units of {self.cryptocurrency.name}.")
        if self.order_type == "BUY":
            total_cost = self.amount * self.cryptocurrency.price_per_unit
            self.trader.trade(self.cryptocurrency.name, total_cost)
        elif self.order_type == "SELL":
            print("Sell order execution logic goes here.")
