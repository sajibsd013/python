class BankAccount:
    def __init__(self, account_number, name, initial_balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ${amount}")
            print(f"${amount} deposited successfully!")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount}")
            print(f"${amount} withdrawn successfully!")
        else:
            print("Insufficient balance or invalid amount!")

    def check_balance(self):
        print(f"Account Balance: ${self.balance}")

    def transaction_history(self):
        if self.transactions:
            print("Transaction History:")
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No transactions yet.")
