"""
In Python, the behavior of the operators is defined by special methods.
Let's change the behavior of the operators with user defined classes.

Operator    Method          Action
------------------------------------------------------
+           __add__         addition
-           __sub__         substraction
*           __mul__         multiplication
/           __div__         division
//          __floordiv__    full division
%           __mod__         module
**          __pow__         potency
+           __pos__         positive
-           __neg__         negative
<           __lt__          lesser than
>           __gt__          greater than
<=          __le__          lesse or equal to
>=          __ge__          greater or equal to
==          __eq__          equal to
!=          __ne__          different than
<<          __lshift__      move to left
>>          __rshift__      move to right
&           __and__         and bit-a-bit
|           __or__          or bit-a-bit
^           __xor__         exclusive or bit-a-bit
~           __inv__         invertion
"""


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):
        return f"<class 'Rectangle({self.x}, {self.y})'>"

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Rectangle(new_x, new_y)

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = r1 + r2
print(r1 == r3)
