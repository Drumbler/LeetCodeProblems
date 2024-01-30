class ReverseBits(object):
    def reverseBits(self, n):
        reversed_n = 0
        for i in range(32):
            last = n % 2
            reversed_n = reversed_n * 2 + last
            n = n // 2
        return reversed_n


s = ReverseBits()
print(s.reverseBits(0b00000010100101000001111010011100))
