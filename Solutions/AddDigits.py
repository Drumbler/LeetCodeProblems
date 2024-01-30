class AddDigits:
    def add_digits(self, num: int):
        res = num
        num = str(num)
        while len(num) > 1:
            res = 0
            for i, c in enumerate(num):
                res += int(num[i])
            num = str(res)
        return res


s = AddDigits()
print(s.add_digits(38))
