from lesson_7.objects import ShoppingCart, Product

cart = ShoppingCart()

p1 = Product('Shirt', 50)
p2 = Product('Iphone', 10000)
p3 = Product('Mug', 15)

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)
cart.list_products()
print(cart.total_price())