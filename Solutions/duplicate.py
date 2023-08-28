class duplicate(object):
    def containsDuplicate(self, nums):
        # nums_dict = set()
        # for i in range(0, len(nums)):
        #     if nums[i] in nums_dict:
        #         return True
        #     else:
        #         nums_dict.add(nums[i])
        # return False
        ################################################
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == nums[i]:
        #             return True
        # return False
        ##########################
        return len(set(nums)) < len(nums)


s = duplicate()
print(s.containsDuplicate([2,14,18,22,22]))
