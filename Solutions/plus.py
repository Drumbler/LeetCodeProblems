class plus(object):
    def plusOne(self, digits):
        dig = len(digits) - 1
        if digits[dig] + 1 >= 10:
            digits[dig - 1] += 1
            digits[dig] = 0
            for i in range(dig, -1, -1):
                if digits[i] >= 10:
                    digits[i - 1] += 1
                    digits[i] = 0
        else:
            digits[len(digits) - 1] += 1
        return digits


s = plus()
print(s.plusOne([9, 9, 9, 9, 9, 9]))
