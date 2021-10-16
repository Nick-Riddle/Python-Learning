import os
import tempfile
import sys
import random


class File:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                pass

    def read(self):
        with open(self.path, 'r') as f:
            f.seek(0)
            return f.read()

    def write(self, string):
        with open(self.path, 'r+') as f:
            if f.read() != '':
                f.write(f.read() + '\n' + string)
            else:
                f.write(string)

    def __add__(self, other):
        if isinstance(other, File):
            number = random.randint(0, 10)
            while os.path.exists(os.path.join(tempfile.gettempdir(), 'storage_new_' + str(number))):
                number = random.randint(0, 10)
            new_file = File(os.path.join(tempfile.gettempdir(), 'storage_new_') + str(number))
            new_file.write(self.read() + '\n' + other.read())
            return new_file

    def __str__(self):
        return self.path