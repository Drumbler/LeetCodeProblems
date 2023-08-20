class canPlaceFlowers(object):
    def canPlaceFlowers(self, flowerbed, n):
        m = 1

        flowerbed.append(0)
        flowerbed.append(1)

        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                m += 1
            else:
                n -= (m - 1) // 2
                if n <= 0:
                    return True
                m = 0
        return False


s = canPlaceFlowers()
print(s.canPlaceFlowers([
    0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 5))
