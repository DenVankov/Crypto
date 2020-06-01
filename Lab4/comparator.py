def compare(filename1, filename2):
    file1 = open(filename1, 'r')
    file2 = open(filename2, 'r')
    text1 = file1.read()
    text2 = file2.read()
    size = len(text1)
    size2 = len(text2)

    if size > size2:
        size = size2

    success = 0
    for i in range(size):
        if text1[i] == text2[i]:
            success += 1

    accuracy = success / size

    file1.close()
    file2.close()
    return accuracy


def without_space_compare(filename1, filename2):
    file1 = open(filename1, 'r')
    file2 = open(filename2, 'r')
    text1 = file1.read()
    text2 = file2.read()

    new_text1 = ''
    new_text2 = ''

    for i in text1:
        if i != ' ':
            new_text1 += i

    for i in text2:
        if i != ' ':
            new_text2 += i

    if len(new_text1) > len(new_text2):
        size = len(new_text2)
    else:
        size = len(new_text1)

    success = 0
    for i in range(size):
        if new_text1[i] == new_text2[i]:
            success += 1

    accuracy = success / size

    file1.close()
    file2.close()
    return accuracy


if __name__ == '__main__':
    print('Starting comparing by position in text with spaces')

    print('TEST 1:')
    print(f'Accuracy of clean and generated by symbols: ',
          compare('clean Gone with the Wind.txt', 'clean War and Peace.txt'))
    print('TEST 2:')
    print(f'Accuracy of clean and generated by symbols: ', compare('clean War and Peace.txt', 'text by symbols 1.txt'))
    print('TEST 3:')
    print(f'Accuracy of clean and generated by words: ', compare('clean War and Peace.txt', 'text by words 1.txt'))
    print('TEST 4:')
    print(f'Accuracy of two generated by symbols: ', compare('text by symbols 1.txt', 'text by symbols 2.txt'))
    print('TEST 5:')
    print(f'Accuracy of two generated by words: ', compare('text by words 1.txt', 'text by words 2.txt'), '\n')

    print('Starting comparing by symbols without spaces')

    print('TEST 1:')
    print(f'Accuracy of clean and generated by symbols: ',
          without_space_compare('clean Gone with the Wind.txt', 'clean War and Peace.txt'))
    print('TEST 2:')
    print(f'Accuracy of clean and generated by symbols: ', without_space_compare('clean War and Peace.txt', 'text by symbols 1.txt'))
    print('TEST 3:')
    print(f'Accuracy of clean and generated by words: ', without_space_compare('clean War and Peace.txt', 'text by words 1.txt'))
    print('TEST 4:')
    print(f'Accuracy of two generated by symbols: ', without_space_compare('text by symbols 1.txt', 'text by symbols 2.txt'))
    print('TEST 5:')
    print(f'Accuracy of two generated by words: ', without_space_compare('text by words 1.txt', 'text by words 2.txt'))