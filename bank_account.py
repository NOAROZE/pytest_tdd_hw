class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough balance to withdraw")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def is_empty(self):
        return self.balance == 0