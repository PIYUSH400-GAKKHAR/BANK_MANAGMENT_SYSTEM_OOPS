def deposit_money(self):

    print("\n========== DEPOSIT MONEY ==========")

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
            input("Enter amount to deposit: ")
        )

        account.deposit(amount)

        self.save_data()

        print("Money deposited successfully.")

        print(
            "New Balance: ₹{:.2f}".format(
                account.balance
            )
        )

    except ValueError as e:

        print(e)