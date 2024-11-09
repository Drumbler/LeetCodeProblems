from typing import List
import bisect


def searchInsert(nums: List[int], target: int) -> int:
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


print(searchInsert([1, 3, 5, 6], 7))
