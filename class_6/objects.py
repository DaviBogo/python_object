class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def list_products(self):
        for product in self.products:
            print(product.name, product.price)

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
