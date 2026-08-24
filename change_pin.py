def change_pin(self):

    print("\n========== CHANGE PIN ==========")

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

    old_pin = input("Enter old PIN: ")

    new_pin = input(
        "Enter new 4-digit PIN: "
    )

    try:

        account.change_pin(
            old_pin,
            new_pin
        )

        self.save_data()

        print("PIN changed successfully.")

    except ValueError as e:

        print(e)