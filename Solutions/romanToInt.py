def romanToInt(s: str) -> int:
    roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    res = 0
    for i, c in enumerate(s):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            res -= roman[c]
        else:
            res += roman[c]
    return res


print(romanToInt("VIII"))
