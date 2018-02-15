from os import walk
from os.path import expanduser, join
import re
from re import match


def math_file_in_list(file_list, pattern):
    result = []
    for file_name in file_list:
        if match(pattern, file_name):
            result.append(file_name)
    return result


def find_by_name(name):
    result = []
    for dirpath, dirnames, filenames in walk('.'):
        names = math_file_in_list(filenames, name)
        result.extend(names)

    return result

def change(name):
    tmp = re.sub('\*', '\w+',name)
    return tmp

def do():
    to_find = input('type file name you want to find: ')
    to_find = change(to_find)
    print(to_find)
    result = find_by_name(to_find)
    message = "I found:\n {}"
    if not result:
        print(message.format('nothing'))
    else:
        print(message.format('\n'.join(result)))


if __name__ == '__main__':
    do()
