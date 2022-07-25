"""
Polimorfism is the principle that allows children classes from the 
same super class to inherit the same methods (with the same signature)
but with different behavior.
Same Signature = equal quantity and type of parameters
"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def talk(self, msg): pass


class B(A):
    def talk(self, msg):
        print(f'B is talking...{msg}')


class C(A):
    def talk(self, msg):
        print(f'C is talking...{msg}')


b = B()
c = C()
b.talk('Subject')
c.talk('Other subject')
