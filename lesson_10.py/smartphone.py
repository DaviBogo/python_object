from eletronic import Eletronic
from log import LogMixin


class Smartphone(Eletronic, LogMixin):
    def __init__(self, name):
        super().__init__(name)
        self.connected = False

    def connect(self):
        if not self._on:
            error = f'{self._name} is not on.'
            print(error)
            self.log_error(error)
            return

        if self.connected:
            error = f'{self._name} is already connected.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._name} is connected...'
        print(info)
        self.log_info(info)
        self.connected = True

    def disconnect(self):
        if not self.connected:
            error = f'{self._name} is already not connected.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._name} is discnnected...'
        self.log_info(info)
        self.connected = False
