class FindTheDifference:
    def find_the_difference(self, s, t):
        sum1 = 0
        sum2 = 0
        for i in s:
            sum2 += ord(i)
        for i in t:
            sum1 += ord(i)
        return chr(sum1 - sum2)


s = FindTheDifference()
print(s.find_the_difference('abcd', 'abcde'))
