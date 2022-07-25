from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, account, balance):
        self._agency = agency
        self._account = account
        self._balance = balance

    @property
    def agency(self):
        return self._agency

    @property
    def account(self):
        return self._account

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            return ValueError('Balance must be numeric')

        self._balance = value

    def deposit(self, value):
        if not isinstance(value, (int, float)):
            return ValueError('Balance must be numeric')

        self._balance += value
        self.details()

    @abstractmethod
    def withdraw(self, value):
        pass

    def details(self):
        print(f'Agency: {self._agency}', end=' ')
        print(f'Account: {self._account}', end=' ')
        print(f'Balance: {self._balance}')
