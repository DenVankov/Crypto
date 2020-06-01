from random import randint
from random import choice


def generate_by_symbols(filename, vocabulary, length):
    file = open(filename, 'w')

    out_len = 0
    while out_len < length:
        word_size = randint(1, 20)
        generated_word = ''
        for _ in range(word_size):
            symbol = choice(vocabulary)
            generated_word += symbol

        if out_len + word_size > length:
            file.write(generated_word[0:length - out_len + 1])
            out_len += length - out_len + 1
        else:
            file.write(generated_word + ' ')
            out_len += word_size + 1

    print(f'Previous  size = {length}')
    print(f'Generated size = {out_len}')
    file.close()


def generate_by_words(filename, vocabulary, length):
    file = open(filename, 'w')

    out_len = 0

    while out_len < length:
        word = choice(vocabulary)
        if out_len + len(word) > length:
            file.write(word[:length-out_len + 1])
            out_len += length - out_len + 1
        else:
            file.write(word + ' ')
            out_len += len(word) + 1

    print(f'Previous  size = {length}')
    print(f'Generated size = {out_len}')
    file.close()


if __name__ == '__main__':
    text = open('clean War and Peace.txt', 'r').read()
    len_ = len(text)

    alphabet = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
    set_ = []
    for i in alphabet[0]:
        set_.append(i)
    set_ = sorted(set_)
    print(f'Alphabet is:\n{set_}')

    print(f'Full length of all text data is: {len_} characters')
    vocabulary = sorted(set(text))
    print(f'With {len(vocabulary)} unique characters')
    print(f'Vocabulary is:\n{vocabulary}')

    generate_by_symbols('text by symbols 1.txt', set_, len_)
    generate_by_symbols('text by symbols 2.txt', set_, len_)

    words = []

    word = ''
    for symb in text:
        if symb != ' ':
            word += symb
        else:
            words.append(word)
            word = ''
    words_set = sorted(set(words))
    print(f'Unique words in text: {len(words_set)}')
    print(f'Example of words\n {words_set[1000:1020]}')

    generate_by_words('text by words 1.txt', words_set, len(text))
    generate_by_words('text by words 2.txt', words_set, len(text))


