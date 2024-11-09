import bisect
import timeit
from typing import List


def search() -> int:
    nums = [-1, 0, 3, 5, 6, 12]
    target = 3

    high = len(nums) - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1


def search_v2() -> int:
    nums = []
    target = 3

    guess = bisect.bisect_left(nums, target)
    if target == nums[guess]:
        return guess
    else:
        return -1


def search_v3() -> int:
    nums = []
    target = 3

    i = bisect.bisect_left(nums, target)
    print(i)
    if i != len(nums) and nums[i] == target:
        return i
    return -1


print(search_v3())

# print(timeit.timeit(search, number=1000000))
# print(timeit.timeit(search_v2, number=1000000))
# print(timeit.timeit(search_v3, number=1000000))
