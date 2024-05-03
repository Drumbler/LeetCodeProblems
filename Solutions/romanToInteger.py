class romanToInteger(object):
    def romanToInt(self, s):
        r_integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        res = 0
        for i, c in enumerate(s):
            if i + 1 < len(s) and r_integers[s[i]] < r_integers[s[i + 1]]:
                res -= r_integers[c]
            else:
                res += r_integers[c]
        return res


s = romanToInteger()
print(s.romanToInt('VIII'))

# import itertools

# a = (i for i in range(5))
# x, y = itertools.tee(a, 2)
# next(y)

# for c, n in itertools.zip_longest(x, y, fillvalue=''):
#     print(c, n)
