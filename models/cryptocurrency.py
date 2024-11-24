class Cryptocurrency:
    def __init__(self, name, symbol, price_per_unit):
        self.name = name
        self.symbol = symbol
        self.price_per_unit = price_per_unit

    def __repr__(self):
        return f"Cryptocurrency(name='{self.name}', symbol='{self.symbol}', price_per_unit={self.price_per_unit})"

    def __str__(self):
        return f"{self.name} ({self.symbol}) - Price per unit: {self.price_per_unit}"
