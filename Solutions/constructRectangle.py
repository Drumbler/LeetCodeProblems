from math import sqrt
from typing import List


def constructRectangle(area: int) -> List[int]:
    l: int
    w: int
    sqrt_area = int(sqrt(area))
    if sqrt_area ** 2 == area:
        return [sqrt_area, sqrt_area]

    for w in range(sqrt_area, 0, -1):
        if area % w == 0:
            l = area // w
            return [l, w]
    return False


print(constructRectangle(37))
