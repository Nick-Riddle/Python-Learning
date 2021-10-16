from solution import FileReader


def _main():
    reader = FileReader('new_txt.txt')
    print(reader.read())


if __name__ == '__main__':
    _main()