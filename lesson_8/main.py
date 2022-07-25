"""
Association - uses | Aggregation - has | Composition - owns | Heritage - is
"""

from objects import *

client = Client('Davi', 22)
client.speak()
print(client.class_name)
client.buy()

print()

client_vip = ClientVIP('Érica', 21, 'Scherner')
client_vip.speak()