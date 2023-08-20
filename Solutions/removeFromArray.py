class removeFromeArray(object):
    def removeDuplicates(self, nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)


s = removeFromeArray()
print(s.removeDuplicates([1, 1, 2]))
