# **Cryptocurrency Exchange System**

A Python-based cryptocurrency exchange system that simulates trading operations, user wallets, and administrative controls. This project demonstrates object-oriented programming concepts, including inheritance, composition, abstract classes, and mixins.

---

## **Features**
- **Users**: 
  - Traders can trade cryptocurrencies and manage their wallets.
  - Admins can manage the exchange system.
- **Cryptocurrencies**: 
  - Manage and use different cryptocurrencies with unique properties (name, symbol, price).
- **Wallets**: 
  - Store and manage cryptocurrency balances for traders.
- **Orders**: 
  - Place buy and sell orders for cryptocurrencies.
- **Data Validation**: 
  - Validates inputs like balances, amounts, and cryptocurrency details.
- **Random User IDs**: 
  - Automatically generates unique user IDs for each user.

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/shalvazak/cryptocurrency-exchange-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd cryptocurrency-exchange-system
   ```
3. Ensure you have Python 3.7+ installed on your system.

---

## **Usage**
1. Run the `main.py` file to simulate the cryptocurrency exchange system:
   ```bash
   python main.py
   ```
2. Example outputs include:
   - User information
   - Wallet contents
   - Cryptocurrency transactions

---

## **Project Structure**
```
cryptocurrency-exchange-system/
├── main.py                  # Entry point of the application
├── models/
│   ├── cryptocurrency.py    # Cryptocurrency class
│   ├── wallet.py            # Wallet class
│   ├── order.py             # Order handling class
├── users/
│   ├── base_user.py         # Abstract base AccountUser class
│   ├── trader.py            # Trader class
│   ├── admin.py             # Admin class
├── mixins/
│   ├── transaction_mixin.py # TransactionMixin for reusable logic
├── utils/
│   ├── validations.py       # Validation helper functions
└── README.md                # Project documentation (this file)
```

---

## **How It Works**
### **1. User Management**
- **Trader**:
  - Can trade cryptocurrencies, deposit funds, and view wallet contents.
- **Admin**:
  - Can manage the exchange but doesn't participate in trading.

### **2. Cryptocurrency**
- Cryptocurrencies are defined with:
  - **Name**: e.g., Bitcoin.
  - **Symbol**: e.g., BTC.
  - **Price**: e.g., 50,000 USD/unit.

### **3. Wallets**
- Wallets store cryptocurrencies and allow traders to manage balances.

### **4. Orders**
- Buy or sell cryptocurrencies via `Order` objects.

---

## **Example**
Here's how you might use the system programmatically:

```python
from users.trader import Trader
from models.cryptocurrency import Cryptocurrency
from models.wallet import Wallet
from models.order import Order

# Create a trader
trader = Trader(username="CryptoKing", balance=10000)

# Add cryptocurrencies to wallet
wallet = Wallet(trader=trader)
bitcoin = Cryptocurrency(name="Bitcoin", symbol="BTC", price_per_unit=50000)
wallet.add_crypto(bitcoin, 0.1)

# View wallet contents
wallet.view_wallet()

# Execute a buy order
order = Order(trader=trader, cryptocurrency=bitcoin, amount=0.05, order_type="BUY")
order.execute()
```

---

## **Concepts Used**
- **Object-Oriented Programming**:
  - Abstract Base Classes, Inheritance, Composition.
- **Design Patterns**:
  - Mixin pattern for reusable functionality.
- **Data Validation**:
  - Centralized validation in `utils/validations.py`.
- **Encapsulation**:
  - Protected (`_attribute`) and private (`__attribute`) attributes.
- **Error Handling**:
  - Handles invalid inputs and insufficient balances gracefully.

---

## **Future Enhancements**
- Integrate with real-world cryptocurrency price APIs (e.g., CoinGecko).
- Add logging and analytics for user activities.
- Expand order types (e.g., limit orders).
- Implement unit tests for comprehensive validation.

---


## **Contributors**
- **Shalva Zakalashvili**  
  *Developer*  

Feel free to contribute by submitting pull requests or reporting issues!
