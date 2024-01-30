class plus(object):
    def plusOne(self, digits):
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] >= 10:
                if not i:
                    return [1] + [0] * len(digits)
                digits[i - 1] += 1
                digits[i] = 0
            else:
                break
        return digits


s = plus()
print(s.plusOne([9, 9, 9, 9]))
