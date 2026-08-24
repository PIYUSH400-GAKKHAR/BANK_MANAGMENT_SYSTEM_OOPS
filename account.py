class Account:

    
    def __init__(self, account_no, name, pin, balance=0):
        self.account_no = account_no
        self.name = name
        self._pin = pin
        self.balance = balance
        self.transactions = []

    def check_pin(self, pin):
        return self._pin == pin

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        self.balance += amount
        self.add_transaction(f"Deposited ₹{amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        self.add_transaction(f"Withdrawn ₹{amount:.2f}")

    def add_transaction(self, message):
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.transactions.append(f"{time} - {message}")

    def change_pin(self, old_pin, new_pin):

        if not self.check_pin(old_pin):
            raise ValueError("Old PIN is incorrect.")

        if len(new_pin) != 4 or not new_pin.isdigit():
            raise ValueError("PIN must contain exactly 4 digits.")

        self._pin = new_pin

    def display_details(self):
        print("\n---------- ACCOUNT DETAILS ----------")
        print("Account Number :", self.account_no)
        print("Account Holder :", self.name)
        print("Balance        : ₹{:.2f}".format(self.balance))
        print("-------------------------------------")

    def display_transactions(self):

        print("\n---------- TRANSACTION HISTORY ----------")

        if not self.transactions:
            print("No transactions found.")
        else:
            for transaction in self.transactions:
                print(transaction)

        print("-----------------------------------------")
