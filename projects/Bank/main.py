from management import BankManagementSystem

def main():
    system = BankManagementSystem()

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Show All Accounts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            acc_num = input("Enter account number: ")
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))
            system.create_account(acc_num, name, initial_balance)


        elif choice == '2':
            acc_num = input("Enter account number: ")
            account = system.get_account(acc_num)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)

            else:
                print("Account not found!")

        elif choice == '3':
            acc_num = input("Enter account number: ")
            account = system.get_account(acc_num)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)

            else:
                print("Account not found!")

        elif choice == '4':
            acc_num = input("Enter account number: ")
            account = system.get_account(acc_num)
            if account:
                account.check_balance()
            else:
                print("Account not found!")

        elif choice == '5':
            acc_num = input("Enter account number: ")
            account = system.get_account(acc_num)
            if account:
                account.transaction_history()
            else:
                print("Account not found!")

        elif choice == '6':
            system.show_all_accounts()

        elif choice == '7':
            print("Exiting the system. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
