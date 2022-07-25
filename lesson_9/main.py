"""
Multi-Heritage
"""

class A:
    def do_something(self):
        print('doing something... In A.')


class B(A):
    def do_something(self):
        print('doing something... in B.')


class C(A):
    def do_something(self):
        print('doing something... in C.')


class D(B, C):
    pass


class E(C, B):
    pass


d = D()
d.do_something()

e = E()
e.do_something()
