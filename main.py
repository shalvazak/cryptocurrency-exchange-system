from users.trader import Trader
from users.admin import Admin
from models.cryptocurrency import Cryptocurrency
from models.wallet import Wallet
from models.order import Order

# Create users
trader = Trader(username="CryptoKing", balance=10000)
admin = Admin(username="AdminPro", admin_level=1)

# Create cryptocurrencies
bitcoin = Cryptocurrency(name="Bitcoin", symbol="BTC", price_per_unit=50000)
ethereum = Cryptocurrency(name="Ethereum", symbol="ETH", price_per_unit=3000)

# Trader actions
wallet = Wallet(trader=trader)
wallet.add_crypto(bitcoin, 0.1)
wallet.add_crypto(ethereum, 2)
wallet.view_wallet()

# Admin actions
admin.manage_exchange()

# Place and execute an order
order = Order(trader=trader, cryptocurrency=ethereum, amount=1, order_type="BUY")
order.execute()

# Trader deposits more balance
trader.deposit(5000)
