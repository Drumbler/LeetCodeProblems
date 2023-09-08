class subsequence(object):
    def isSubsequence(self, s, t):
        res = 0
        if len(s) > len(t):
            return False

        for i in range(len(t)):
            if res >= len(s):
                break
            if s[res] == t[i]:
                res += 1
        return res == len(s)


s = subsequence()
print(s.isSubsequence('abc', 'ahbgdc'))
