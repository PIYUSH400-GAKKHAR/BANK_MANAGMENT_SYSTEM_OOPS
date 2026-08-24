def main():

    bank = Bank()

    while True:

        print("\n")
        print("==========================================")
        print("        BANK MANAGEMENT SYSTEM")
        print("==========================================")

        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Account Details")
        print("7. Transaction History")
        print("8. Change PIN")
        print("9. Close Account")
        print("10. Exit")

        print("==========================================")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            bank.create_account()

        elif choice == "2":

            bank.deposit_money()

        elif choice == "3":

            bank.withdraw_money()

        elif choice == "4":

            bank.check_balance()

        elif choice == "5":

            bank.transfer_money()

        elif choice == "6":

            bank.account_details()

        elif choice == "7":

            bank.transaction_history()

        elif choice == "8":

            bank.change_pin()

        elif choice == "9":

            bank.close_account()

        elif choice == "10":

            print(
                "\nThank you for using "
                "Bank Management System!"
            )

            break

        else:

            print(
                "Invalid choice. Please try again."
            )











if __name__ == "__main__":
    main()