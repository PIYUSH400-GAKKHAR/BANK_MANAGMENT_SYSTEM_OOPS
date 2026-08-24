def transfer_money(self):

    print("\n========== TRANSFER MONEY ==========")

    try:
 
        sender_no = int(
            input("Enter your account number: ")
        )

        receiver_no = int(
            input("Enter receiver account number: ")
        )

    except ValueError:

        print("Invalid account number.")
        return

    sender = self.find_account(sender_no)

    receiver = self.find_account(receiver_no)

    if sender is None:

        print("Sender account not found.")
        return

    if receiver is None:

        print("Receiver account not found.")
        return

    if sender_no == receiver_no:

        print(
            "Cannot transfer money to the same account."
        )

        return

    pin = input("Enter your PIN: ")

    if not sender.check_pin(pin):

        print("Incorrect PIN.")
        return

    try:

        amount = float(
            input("Enter amount to transfer: ")
        )

        if amount <= 0:

            raise ValueError(
                "Amount must be greater than 0."
            )

        if amount > sender.balance:

            raise ValueError(
                "Insufficient balance."
            )

        sender.balance -= amount

        receiver.balance += amount

        sender.add_transaction(
            f"Transferred ₹{amount:.2f} "
            f"to Account {receiver_no}"
        )

        receiver.add_transaction(
            f"Received ₹{amount:.2f} "
            f"from Account {sender_no}"
        )

        self.save_data()

        print("\nTransfer successful!")

        print(
            "Transferred Amount: ₹{:.2f}".format(
                amount
            )
        )

        print(
            "Remaining Balance: ₹{:.2f}".format(
                sender.balance
            )
        )

    except ValueError as e:

        print(e)
