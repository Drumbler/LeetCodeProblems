class PowerOfFour:
    def is_power_of_four(self, n: int) -> bool:
        if n == 1:
            return True
        res = 4
        while res < n:
            res *= 4

        return n == res


s = PowerOfFour()
print(s.is_power_of_four(256))
