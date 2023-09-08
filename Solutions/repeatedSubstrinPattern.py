class repeatedPattern(object):
    def repeatedSubstringPattern(self, s):
        for l in range(1, len(s) // 2 + 1):
            if len(s) % l != 0:
                continue
            sub = s[0:l]

            ok = True
            for j in range(l, len(s), l):
                if sub != s[j:j + l]:
                    ok = False
                    break
            if ok:
                return True
        return False


s = repeatedPattern()
print(s.repeatedSubstringPattern('abab'))
