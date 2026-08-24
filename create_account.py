def create_account(self):

    print("\n========== CREATE ACCOUNT ==========")

    name = input("Enter account holder name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    pin = input("Create 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return
 
    try:

        initial_deposit = float(
            input("Enter initial deposit: ")
        )

        if initial_deposit < 0:
            print("Deposit cannot be negative.")
            return

    except ValueError:

        print("Please enter a valid amount.")
        return

    account_no = self.next_account_no

    self.next_account_no += 1

    account = SavingsAccount(
        account_no,
        name,
        pin,
        initial_deposit
    )

    if initial_deposit > 0:

        account.add_transaction(
            f"Initial deposit ₹{initial_deposit:.2f}"
        )

    self.accounts[account_no] = account

    self.save_data()

    print("\nAccount created successfully!")

    print(
        "Your Account Number is:",
        account_no
    )
