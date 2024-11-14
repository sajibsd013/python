from accounts import BankAccount


class BankManagementSystem:
    def __init__(self):
        self.accounts = {}
    def create_account(self, account_number, name, initial_balance=0.0):
        if account_number not in self.accounts:
            account = BankAccount(account_number, name, initial_balance)
            self.accounts[account_number] = account
            print(f"Account created for {name} with account number {account_number}.")
        else:
            print("Account already exists!")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def show_all_accounts(self):
        if not self.accounts:
            print("No accounts in the system.")
        else:
            print("Bank Accounts:", self.accounts)
            for account in self.accounts.values():
                print(f"Account Number: {account.account_number}, Name: {account.name}, Balance: ${account.balance}")
