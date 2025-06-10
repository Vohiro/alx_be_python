class BankAccount:
    def __init__(self, account_balance=0):
        # Initialize account_balance (defaults to 0 if not provided)
        self.account_balance = account_balance
        
    def deposit(self, amount):
        self.account_balance += amount
        
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            success = True
        else:
            success = False
        return success
        
    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance)}")
