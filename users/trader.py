from users.base_user import AccountUser
from mixins.transaction_mixin import TransactionMixin


class Trader(AccountUser, TransactionMixin):
    def __init__(self, username, balance, user_id=None):
        super().__init__(user_id, username)
        self._balance = self._validate_balance(balance)

    def get_user_details(self):
        return {"UserID": self._user_id, "Username": self.get_username(), "Balance": self._balance}

    @staticmethod
    def _validate_balance(balance):
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Balance must be a non-negative number.")
        return balance

    def trade(self, cryptocurrency, amount):
        if amount > self._balance:
            raise ValueError("Insufficient balance.")
        self._balance -= amount
        print(f"Trader {self.get_username()} traded {amount} units of {cryptocurrency}.")

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")
