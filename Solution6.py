# Не решено, не получилось пока что
class Solution6(object):
    def singleNumber(self, nums):
        # for v in nums:
        #     if nums.count(v) == 1:
        #         return v
        # nums_dict = dict.fromkeys(nums,0)
        # for v in nums:
        #     nums_dict[v] += 1

        nums_dict = {}

        for v in nums:
            nums_dict[v] = nums_dict.get(v, 0) + 1

        for k, v in nums_dict.items():
            if v == 1:
                return k

        print(nums_dict)


s = Solution6()
print(s.singleNumber([2, 2, 1, 1, 4, 5, 5]))
