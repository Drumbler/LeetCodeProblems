class Solution7(object):
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            print(nums)
        return nums


s = Solution7()
print(s.moveZeroes([1, 0, 0, 3, 4]))
