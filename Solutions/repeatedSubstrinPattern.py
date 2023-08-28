class repeatedPattern(object):
    def repeatedSubstringPattern(self, s):
        for l in range(1, len(s) // 2 + 1):
            if len(s) % l != 0:
                continue
            sub = s[0:l]
            print(sub)
            for j in range(l, len(s), l):
                c = 0
                if sub != s[j:j + l]:
                    c += 1
                    break
            if c == 0:
                return True
        return False


s = repeatedPattern()
print(s.repeatedSubstringPattern('abab'))
