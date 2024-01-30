class AddBinary(object):
    def addBinary(self, a: str, b: str):
        res = []
        carry = 0
        ind_a = len(a) - 1
        ind_b = len(b) - 1
        while ind_a >= 0 or ind_b >= 0 or carry:
            if ind_a >= 0:
                carry += int(a[ind_a])
                ind_a -= 1
            if ind_b >= 0:
                carry += int(b[ind_b])
                ind_b -= 1
            res.append(str(carry % 2))
            carry //= 2
        return ''.join(reversed(res))


s = AddBinary()
print(s.addBinary('1', '111'))
