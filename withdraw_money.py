def withdraw_money(self):

    print("\n========== WITHDRAW MONEY ==========")
 
    try:

        account_no = int(
            input("Enter account number: ")
        )

    except ValueError:

        print("Invalid account number.")
        return

    account = self.find_account(account_no)

    if account is None:

        print("Account not found.")
        return

    pin = input("Enter PIN: ")

    if not account.check_pin(pin):

        print("Incorrect PIN.")
        return

    try:

        amount = float(
            input("Enter amount to withdraw: ")
        )

        account.withdraw(amount)

        self.save_data()

        print("Money withdrawn successfully.")

        print(
            "Remaining Balance: ₹{:.2f}".format(
                account.balance
            )
        )

    except ValueError as e:

        print(e)
