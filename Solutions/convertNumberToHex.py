class convertNumberToHex:
    def toHex(self, num: int):
        hex_nums = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }
        result = []
        if num < 0:
            num = num + 0x100000000
        elif num == 0:
            return "0"
        while num:
            remainder = num % 16
            if remainder > 9:
                result.append(hex_nums[remainder])
            else:
                result.append(str(remainder))
            num //= 16
        return ''.join(result[::-1])


s = convertNumberToHex()
print(s.toHex(0))


# 0x100 = 256 in hexadecimal
