BLOCK = 512


class SHA_1:
    def __init__(self, rounds):
        self.h = (0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0)
        self.rounds = rounds

    def hexDigets(self):
        return '%08x%08x%08x%08x%08x' % self.h

    @staticmethod
    def getChunk(text):
        return [text[i:i + BLOCK] for i in range(0, len(text), BLOCK)]

    @staticmethod
    def leftRotation(n, k):
        return ((n << k) | (n >> (
                32 - k))) & 0xffffffff  # << mean bitwise left shift on k  , >> mean bitwise right shift on (32 - k). | mean or

    def process(self, chunk):
        h0 = self.h[0]
        h1 = self.h[1]
        h2 = self.h[2]
        h3 = self.h[3]
        h4 = self.h[4]

        W = []

        for i in range(16):
            W.append(int(chunk[i * 32: i * 32 + 32], 2))
        for i in range(16, 80):
            W.append(self.leftRotation(W[i - 3] ^ W[i - 8] ^ W[i - 14] ^ W[i - 16], 1))  # ^ mean XOR

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        # Main loop
        for i in range(self.rounds):
            if (0 <= i <= 19):
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif (20 <= i <= 39):
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif (40 <= i <= 59):
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif (60 <= i <= 79):
                f = b ^ c ^ d
                k = 0xCA62C1D6

            tmp = (self.leftRotation(a, 5) + f + e + k + W[i]) & 0xffffffff
            e = d
            d = c
            c = (self.leftRotation(b, 30))
            b = a
            a = tmp

        # Add this chunk's hash to result so far
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

        self.h = (h0, h1, h2, h3, h4)

    def update(self, message):
        new_msg = ''

        for i in range(len(message)):
            new_msg += '{0:08b}'.format(ord(message[i]))

        len_msg = len(new_msg)
        new_msg += '1'
        while len(new_msg) % 512 != 448:
            new_msg += '0'
        new_msg += '{0:064b}'.format(len_msg)

        chunks = self.getChunk(new_msg)
        for each in chunks:
            self.process(each)

        return self


def algo(rounds, text):
    return SHA_1(rounds).update(text).hexDigets()


if __name__ == '__main__':
    print("Input rounds to start (<= 80): ", end='')
    rounds = int(input())
    print("Input text to start:")
    text = str(input())
    print("Algo: ", algo(rounds, text))
