from sys import argv
from os.path import getsize

def count_number_of_bytes(path: str) -> int:
    return getsize(path)

def count_number_of_lines(path: str) -> int:
    with open(path, 'r', encoding='utf-8') as file:
        return len(file.readlines())

def count_number_of_words(path: str) -> int:
    number_of_words = 0
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
        lines = data.split()    # each word is placed in a separate line
        number_of_words += len(lines)
        return number_of_words

# TODO
def count_number_of_characters():
    pass

# TODO
def count_with_default_option():
    pass


if __name__ == '__main__':

    options = {
        '-c': lambda path : count_number_of_bytes(path),
        '-l': lambda path : count_number_of_lines(path),
        '-w': lambda path : count_number_of_words(path)
    }

    input_option = argv[1]
    file_path = repr(argv[2])[1:-1]

    for option, func in options.items():
        if input_option == option:
            print(str(func(file_path)), file_path)
