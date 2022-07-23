from person import Person

p1 = Person('Davi', 22)
p2 = Person.by_birth_year('Érica', 2001)
print(p2.name, p2.age)
print(p2.id_generator())

p1.eat('apple')
p1.speak('cars')
p1.stop_eating()
p2.speak('films')
p2.eat('honey')
p1.eat('pasta')
p2.stop_speaking()
p1.stop_eating()
p1.speak('cars')
