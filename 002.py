""" 1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

string = input('Введите строку:')

sum_substring = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        sum_substring.add(hash_str)


print(f'{len(sum_substring) - 1} различных подстрок в строке {string}')


""" 2. Закодируйте любую строку по алгоритму Хаффмана."""
from collections import Counter


class Node:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, code_s=dict(), code=''):

    if root is None:
        return

    if isinstance(root.value, str):
        code_s[root.value] = code
        return code_s

    get_code(root.left, code_s, code + '0')
    get_code(root.right, code_s, code + '1')

    return code_s


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])

        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])

        else:
            node.right = spam[1][0]

        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0]


def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

    return res


def decoding(string, codes):
    res = ''
    i = 0

    while i < len(string):

        for code in codes:

            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])

    return res


my_string = input('Введите строку для сжатия: ')
tree = get_tree(my_string)

codes = get_code(tree)
print(f'Шифр: {codes}')

coding_str = coding(my_string, codes)
print('Сжатая строка: ', coding_str)

decoding_str = decoding(coding_str, codes)
print('Исходная строка: ', decoding_str)

if my_string == decoding_str:
    print('Успешно!')
else:
    print('Ошибка!')
