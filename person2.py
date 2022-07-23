from flask import current_app


from random import randint

class Person2:
    current_year = 2022
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_birth_date(self):
        print(self.current_year, self.age)
        
    @classmethod
    def by_birth_year(cls, name, year):
        age = cls.current_year - year
        return cls(name, age)
    
    @staticmethod
    def id_generator():
        rand = randint(10000, 19999)
        return rand
    
p2 = Person2.by_birth_year('Érica', 2001)
print(p2.name, p2.age)
print(p2.id_generator())