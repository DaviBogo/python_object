class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_name = self.__class__.__name__

    def speak(self):
        print(f'{self.class_name} Speaking...')


class Client(Person):
    def buy(self):
        print(f'{self.class_name} is buying...')


class ClientVIP(Client):
    def __init__(self, name, age, last_name):
        super().__init__(name, age)
        self.last_name = last_name

    def speak(self):
        print(f'{self.name} is VIP')
        super().speak()


class Student(Person):
    def study(self):
        print(f'{self.class_name} is studying...')
