def close_account(self):

    print("\n========== CLOSE ACCOUNT ==========")

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

    if account.balance != 0:

        print(
            "Please withdraw/transfer your "
            "remaining balance first."
        )

        return

    del self.accounts[account_no]

    self.save_data()

    print("Account closed successfully.")
