def transaction_history(self):

    print(
        "\n========== TRANSACTION HISTORY =========="
    )

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

    account.display_transactions()
