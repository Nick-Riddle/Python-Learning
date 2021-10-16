class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ''


def _main():
    reader = FileReader('new_txt.txt')
    print(reader.read())


if __name__ == '__main__':
    _main()
