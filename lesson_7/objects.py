class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.addresses = []

    def add_address(self, city, state):
        self.addresses.append(Address(city, state))

    def list_addresses(self):
        for address in self.addresses:
            print(address.city, address.state)
            
    def __del__(self):
        print(f'{self.name} foi apagado.')


class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __del__(self):
        print(f'{self.city} foi apagado.')