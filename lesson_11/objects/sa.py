from objects.account import Account


class SavingsAccount(Account):
    def withdraw(self, value):
        if self.balance < value:
            return ValueError('Balance must be more than or equal to value.')

        self._balance -= value
        self.details()
