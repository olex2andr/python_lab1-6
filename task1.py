import datetime

class TransactionLogger:
    def __init__(self, min_amount):
        self.min_amount = min_amount

    def __call__(self, func):
        def wrapper(obj, amount):
            result = func(obj, amount)
            if abs(amount) > self.min_amount:
                print(f"{datetime.datetime.now()} | {func.__name__} | {amount}")
            return result
        return wrapper


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @TransactionLogger(min_amount=100)
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    @TransactionLogger(min_amount=100)
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостатньо коштів")
        self.balance -= amount
        return self.balance


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.01, min_balance=0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.min_balance = min_balance

    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("Менше за мінімальний баланс")
        return super().withdraw(amount)


acc = Account("Віталік", 500)
acc.deposit(50)
acc.deposit(200)
acc.withdraw(120)

s_acc = SavingsAccount("Олександр", 1000, interest_rate=0.05, min_balance=300)
s_acc.add_interest()
s_acc.withdraw(400)
