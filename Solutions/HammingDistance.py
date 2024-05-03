class HammingDistance:
    def hamming_distance(self, x: int, y: int):
        num = x ^ y
        res = 0
        while num >= 1:
            if num % 2 == 1:
                res += 1
            num //= 2
        return res


s = HammingDistance()
print(s.hamming_distance(3, 1))

        
