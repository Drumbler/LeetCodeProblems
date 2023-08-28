class squareRoot(object):
    def mySqrt(self, x):
        n = 1
        count = 0
        while x > 0:
            if x - n >= 0:
                x = x - n
                count += 1
                n += 2
            else:
                break
        return count


s = squareRoot()
print(s.mySqrt(256))
