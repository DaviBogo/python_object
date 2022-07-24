"""
public, private, protected
_   = hide attribute (public _)
__  = private attribute (_ClassName__attribute_name)
"""


class DataBase:
    def __init__(self):
        self.__data = {}

    @property
    def data(self):
        return self.__data

    def add_client(self, id, name):
        if 'clients' not in self.__data:
            self.__data['clients'] = {id: name}
        else:
            self.__data['clients'].update({id: name})

    def list_clients(self):
        for id, nome in self.__data['clients'].items():
            print(id, nome)

    def _remove_client(self, id):
        del self.__data['clients'][id]


bd = DataBase()
bd.add_client(1, 'José')
bd.add_client(2, 'Davi')
bd.add_client(3, 'Cleiton')
bd.__data = 'Something'
print(bd.__data)
print(bd._DataBase__data)
print(bd.data)
bd._remove_client(2)
bd.list_clients()
