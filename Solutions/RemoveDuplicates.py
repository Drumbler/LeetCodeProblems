from typing import List


def removeDuplicates(nums: List[int]) -> int:
    # for i in reversed(range(len(nums))):
    #     if len(nums) == 1:
    #         break
    #     if nums[i] == nums[i-1]:
    #         nums.pop(i)
    # return len(nums)
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    nums = nums[0:j]
    print(nums)
    return j


print(removeDuplicates([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 7, 7]))
