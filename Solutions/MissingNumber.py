class MissingNumber:
    def missingNumber(self, nums):
        nums_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i
        actual = 0
        should = 0
        for i in range(len(nums)):
            actual += nums[i]
            should += i
        should += len(nums)
        return should - actual


s = MissingNumber()
print(s.missingNumber([0]))
