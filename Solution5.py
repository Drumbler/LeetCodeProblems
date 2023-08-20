class Solution5(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(0, len(nums)):

            for j in range(0, len(nums)-i-1):
                if nums[j] == val:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            if nums[i] != val:
                k+=1
        for i in range(0, len(nums)-k):
            nums.pop()
        return f'{k}, nums={nums}'
s = Solution5()
print(s.removeElement([5,4,5,3,2,1,1,1,1,1],5))