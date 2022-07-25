"""
class File:
    def __init__(self, file, modo):
        print('opening file')
        self.file = open(file, modo)

    def __enter__(self):
        print('returning file')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('closing file')
        self.file.close()
        # Dealing with the exception
        return True

with File('abc.txt', 'w') as file:
    file.write('Something')
"""
from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    try:
        print('Abrindo arquivo')
        file = open(file, mode)
        yield file
    finally:
        print('Fechando arquivo')
        file.close()


with open('lesson_16/abc.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')
