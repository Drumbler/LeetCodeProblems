class Solution2(object):
    def findComplement(self, num):
        summa = 0
        for i in range(1, num//2+1):
           if num % i == 0:
               summa += i
        return summa == num
s = Solution2()
print(s.findComplement(2))

