"""
Association - uses | Aggregation - has | Composition - owns | Heritage - is
"""

from objects import *

client = Client('Davi', 22)
client.speak()
print(client.class_name)
client.buy()