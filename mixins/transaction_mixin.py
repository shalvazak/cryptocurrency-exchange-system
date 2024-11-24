class TransactionMixin:
    def process_transaction(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Transaction amount must be a positive number.")
        print(f"Processing transaction of {amount} units.")
