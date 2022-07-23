
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percentual):
        self.price = self.price - (self.price * (percentual / 100))

    # Getter
    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$', ''))
        self._price = value

    @name.setter
    def name(self, value):
        self._name = value.title()

p1 = Product('shirt', 50)
p1.discount(10)
print(p1.name, p1.price)

p2 = Product('mug', 'R$15')
p2.discount(10)
print(p2.name, p2.price)
