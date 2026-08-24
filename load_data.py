def load_data(self):

    if not os.path.exists(self.filename):

        return

    try:

        with open(
            self.filename,
            "r"
        ) as file:

            data = json.load(file)

        self.next_account_no = data.get(
            "next_account_no",
            1001
        )

        for account_no, details in data.get(
            "accounts",
            {}
        ).items():

            account = SavingsAccount(

                int(account_no),

                details["name"],

                details["pin"],

                details["balance"],

                details.get(
                    "interest_rate",
                    4
                )
            )

            account.transactions = details.get(
                "transactions",
                []
            )

            self.accounts[
                int(account_no)
            ] = account

    except (
        json.JSONDecodeError,
        KeyError
    ):

        print(
            "Unable to load previous bank data."
        )
        
