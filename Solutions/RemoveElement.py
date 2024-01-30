class RemoveElement(object):
    def removeElement(self, nums: list[int], val: int):
        ind = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ind] = nums[i]
                ind += 1
        return ind
        # while val in nums:
        #     nums.remove(val)
        #
        # print(nums)
        # return len(nums)


s = RemoveElement()
print(s.removeElement([0, 1, 2, 2, 3, 0, 4], 2))
