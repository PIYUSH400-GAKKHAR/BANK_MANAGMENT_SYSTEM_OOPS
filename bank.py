class Bank:

    def __init__(self):

        self.accounts = {}

        self.next_account_no = 1001

        self.filename = "bank_data.json"

        self.load_data()