class removeFromArray(object):
    def removeDuplicates(self, nums):
        # i = 1
        # while i < len(nums):
        #     if nums[i] == nums[i - 1]:
        #         nums.remove()
        #     else:
        #         i+=1
        # return nums

        ##################

        # l = 0
        # for r in range(1, len(nums)):
        #     if nums[l] != nums[r]:
        #         l += 1
        #         nums[l] = nums[r]
        #     r += 1
        # return nums[:l+1]

        ##################

        return len(set(nums))
        # This solution is very expensive in terms of memory


s = removeFromArray()
print(s.removeDuplicates([1,2]))
