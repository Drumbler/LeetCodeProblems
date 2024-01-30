class NumberOf1Bits(object):
    def hammingWeight(self, n: int):
        count = 0
        for i in range(32):
            if n % 2 != 0:
                count += 1
            n = n // 2
        return count


s = NumberOf1Bits()
print(s.hammingWeight(0b00000000000000000000000000001011))
