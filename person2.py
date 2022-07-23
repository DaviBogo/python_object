from flask import current_app


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