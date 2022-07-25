from abc import ABC, abstractmethod
from objects.sa import SavingsAccount
from objects.cc import CheckingAccount


class A(ABC):
    @abstractmethod
    def talk(self):
        pass


class B(A):
    def talk(self):
        print('talking B...')


a = B()

sa = SavingsAccount(1111, 2222, 0)
sa.deposit(10)
sa.withdraw(5)
sa.withdraw(5)
sa.withdraw(1)

print('################################')
cc = CheckingAccount(agency=3333, account=5555, balance=0, limit=500)
cc.deposit(200)
cc.withdraw(250)
cc.deposit(100)
cc.withdraw(550)
cc.withdraw(10)
