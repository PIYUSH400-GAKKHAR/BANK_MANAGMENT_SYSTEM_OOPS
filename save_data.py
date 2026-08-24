def save_data(self):

    data = {
        "next_account_no": self.next_account_no,
        "accounts": {}
    }

    for account_no, account in self.accounts.items():

        data["accounts"][str(account_no)] = {

            "name": account.name,

            "pin": account._pin,

            "balance": account.balance,

            "interest_rate": account.interest_rate,

            "transactions": account.transactions
        }
 
    with open(
        self.filename,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )
