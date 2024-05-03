def roman_to_integer(s):
    roman_ints = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    res = 0
    for i, c in enumerate(s):
        if i + 1 < len(s) and roman_ints[s[i]] < roman_ints[s[i + 1]]:
            res -= roman_ints[s[i]]
        else:
            res += roman_ints[s[i]]
    return res


print(roman_to_integer('IM'))
