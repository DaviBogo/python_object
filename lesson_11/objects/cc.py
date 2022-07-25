from objects.account import Account


class CheckingAccount(Account):
    def __init__(self, agency, account, balance, limit=100):
        super().__init__(agency, account, balance)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def withdraw(self, value):
        if (self.balance + self._limit) < value:
            return ValueError('Balance must be more than or equal to value.')

        self._balance -= value
        self.details()
