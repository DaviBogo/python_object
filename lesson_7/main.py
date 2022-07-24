from calendar import c
from objects import Client, Address

address = Address('Indaial', 'SC')
client0 = Client('Érica', 21)
client0.add_address(address.city, address.state)
print(client0.name)
client0.list_addresses()
del client0
print()

client1 = Client('Davi', 22)
client1.add_address('Blumenau', 'SC')
print(client1.name)
client1.list_addresses()
print()
del client1

client2 = Client('Jefferson', 33)
client2.add_address('Belo Horizonte', 'MG')
client2.add_address('Rio de Janeiro', 'RJ')
print(client2.name)
client2.list_addresses()
print()

client3 = Client('Luis', 19)
client3.add_address('São Paulo', 'SP')
print(client3.name)
client3.list_addresses()
print()

print('############################')
