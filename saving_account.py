class SavingsAccount(Account):

    def __init__(
        self,
        account_no,
        name,
        pin,
        balance=0,
        interest_rate=4
    ):
        super().__init__(
            account_no,
            name,
            pin,
            balance
        )

        self.interest_rate = interest_rate

    def calculate_interest(self):

        interest = self.balance * self.interest_rate / 100

        return interest
class SavingsAccount(Account):


 

super().__init__()
