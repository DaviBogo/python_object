class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_name = self.__class__.__name__
    
    def speak(self):
        print(f'{self.name} Speaking...')


class Client(Person):
    def buy(self):
        print(f'{self.name} is buying...')


class Student(Person):
    def study(self):
        print(f'{self.name} is studying...')
