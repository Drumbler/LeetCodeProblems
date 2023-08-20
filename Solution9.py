class Solution9(object):
    def twoSum(self, nums, target):
        m = {}
        for i in range(0, len(nums)):
            n = target - nums[i]
            if n in m:
                return [m[n], i]
            m[nums[i]] = i


s = Solution9()
print(s.twoSum([3, 2, 4], 6))
