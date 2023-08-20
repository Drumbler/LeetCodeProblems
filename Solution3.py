class Solution3(object):
    def findComplement(self, num):
        a = 0
        m = {
            '0': 1, '1': 0
        }
        for c in bin(num)[2:]:
            a = a * 2 + m[c]
        return a


s = Solution3()
print(s.findComplement(4))
