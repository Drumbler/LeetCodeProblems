

import math


class PowerOfTwo:
    def is_power_of_two(n):
        # if n <= 0:
        #     return False
        # return True if (math.log2(n) % 1 == 0) else False
        return n > 0 and (n & (n - 1)) == 0


s = PowerOfTwo
print(s.is_power_of_two(256))
