from datetime import datetime
from random import randint


class Person:
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def speak(self, subject):
        if self.eating:
            print(f"{self.name} can't speak while eating")
            return
        if self.speaking:
            print(f'{self.name} already speaking')

        print(f'{self.name} is speaking about {subject}')
        self.speaking = True

    def stop_speaking(self):
        if not self.speaking:
            print(f'{self.name} is already not speaking')
            return

        print(f'{self.name} stopped speaking...')
        self.speaking = False

    def eat(self, food):
        if self.eating:
            print(f'{self.name} already eating')
            return
        if self.speaking:
            print(f"{self.name} can't eat while speaking")
            return

        print(f'{self.name} is eating {food}...')
        self.eating = True

    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is already not eating')
            return

        print(f'{self.name} stopped eating...')
        self.eating = False

    def get_birth_date(self):
        return self.current_year - self.age
    
    @classmethod
    def by_birth_year(cls, name, year):
        age = cls.current_year - year
        return cls(name, age)
    
    @staticmethod
    def id_generator():
        rand = randint(10000, 19999)
        return rand
