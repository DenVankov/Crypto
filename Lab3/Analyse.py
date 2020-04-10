import matplotlib.pyplot as plt
import lab3 as sha1
import random
import string
import bitarray


def randomStringDigits(stringLength=40):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for _ in range(stringLength))


def changeLastBit(data):
    arr = bitarray.bitarray()
    arr.frombytes(data.encode('ascii'))
    last_bit = arr[-1]
    if last_bit:
        last_new = bitarray.bitarray('0')
    else:
        last_new = bitarray.bitarray('1')
    ba = arr[:-1]
    ba += last_new
    return bitarray.bitarray(ba.tolist()).tobytes().decode('ascii')


def countBits(n):
    return bin(n).count('1')


if __name__ == '__main__':
    checker = []
    str1 = randomStringDigits()
    str2 = changeLastBit(str1)
    print('First string: ', str1)
    print('First string with changed last bit: ', str2)

    for i in range(0, 81, 4):
        print(f'Current round: {i}')
        str1_new = sha1.algo(i, str1)
        str2_new = sha1.algo(i, str2)
        print('First string with algo: ', str1_new)
        print('First changed string with algo: ', str2_new)
        bits = countBits(int(str1_new, 16) ^ int(str2_new, 16))
        print(f'Number of different bits: {bits}')
        checker.append(bits)

    rounds = [i for i in range(0, 81, 4)]
    for x, y in zip(rounds, checker):
        print(f'Round {x}, different bits: {y}')

    plt.bar(rounds, checker)
    plt.xlabel('Rounds')
    plt.ylabel('Different bits')
    plt.savefig('./fig2.png')
    plt.show()
