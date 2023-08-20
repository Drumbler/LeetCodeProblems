from array import *
class Solution4(object):
    def majorityElement(self, nums):
        x = 0
        for i in range(0, len(nums)):
            if nums[i] > x:
                x = nums[i]
        return(x)
s = Solution4()
print(s.majorityElement([4,5,6,0]))