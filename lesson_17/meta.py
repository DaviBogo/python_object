"""
IN PYTHON EVERYTHING IS A OBJECT: Including classes.
metaclasses are "classes" that create classes.
type is a metaclass (!!!)
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_talk' not in namespace:
            print(f'You should create a method called  b_talk in {name}')
        else:
            if not callable(namespace['b_talk']):
                print(f'b_talk should be a method not a attribute in {name}')

        if 'attr_final' in namespace:
            print(f'{name} tried to override attr_final')
            del namespace['attr_final']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_final = 'Value A'

    def talk(self):
        self.b_talk()


class B(A):
    attr_final = 'Value B'
    b_talk = 'lol'
    # def b_talk(self):
    #     print('hi')
    pass


b = B()
# b.talk()
print(b.attr_final)
