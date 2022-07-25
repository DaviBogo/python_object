class NewError(Exception):
    pass


def test():
    raise NewError('New Error!')


try:
    test()
except NewError as e:
    print(f'Error: {e}')
