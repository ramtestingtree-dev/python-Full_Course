class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"{self.owner}, balance is {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{self.owner}, balance is {self.balance}")

class Savings_Account(Account):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Fund")
        else:
            super().withdraw(amount)

class Current_Account(Account):
    def withdraw(self, amount):
        super().withdraw(amount)

savings = Savings_Account("Ram", 100)
current = Current_Account("Alice", 100)

savings.deposit(1000)
savings.withdraw(1200)
current.deposit(100)
current.withdraw(400)
