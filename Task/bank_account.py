class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    def deposit(self,amount):
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            print(f"(deposit amount must be a positive amount)")
            return False
    def withdraw(self,amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            print(f"Your withdraw counld not go through, insert the correct amount")
            return False
    def get_balance(self):
        print(f"Your current balance is {self.account_balance}")
        