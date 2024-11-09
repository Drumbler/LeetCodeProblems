from typing import List


def removeElement(nums: List[int], val: int) -> int:
    i = 0
    while val in nums:
        if nums[i] == val:
            nums[-1], nums[i] = nums[i], nums[-1]
            nums.pop()
        else: 
            i += 1
    return nums


print(removeElement([3,2,2,3], 3))
