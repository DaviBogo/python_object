from person import Person
from person2 import Person2

p1 = Person('Davi', 22)

p2 = Person2.by_birth_year('Érica', 2001)
print(p2.name, p2.age)
print(p2.id_generator())