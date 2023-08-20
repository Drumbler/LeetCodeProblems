class Solution4Correct(object):
    def majorityElement(self, nums):
        #        nums.sort()
        #        k = len(nums)
        #        return nums[k // 2]
        ############################################

        # x = 0
        # k = 0
        # print(set(nums))
        # for v in set(nums):
        #     n = nums.count(v)
        #     if x < n:
        #         x = n
        #         k = v
        # return k
        ##############################################
        nums_dict = dict.fromkeys(nums, 0)
        for v in nums:
            nums_dict[v] += 1

        k1 = 0
        v1 = 0
        for k, v in nums_dict.items():
            if v > v1:
                v1 = v
                k1 = k
        return k1


s = Solution4Correct()
print(s.majorityElement([4, 5, 5, 3, 3, 3, ]))
