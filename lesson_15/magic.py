# https://rszalski.github.io/magicmethods/

class A:
    def __new__(cls, *args, **kwargs):
        print('New method called.')

        ## SINGLETON
        if not hasattr(cls, '_alreadyexists'):
            cls._alreadyexists = super().__new__(cls)

        return cls._alreadyexists

    def __call__(self, *args, **kwargs):
        return f'Arguments sent: {args} {kwargs}'

    def __len__(self):
        return 55

    def __init__(self, name=None):
        print('INIT')

    def __str__(self):
        return f'What to exibit when this class transforms into a str.'

    def __del__(self):
        print('Colected object.')

    def __setattr__(self, key, value):
        self.__dict__[key] = f'{value} added this to the value'


a = A('Davi Bogo')
