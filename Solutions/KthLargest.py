class KthLargest(object):
    def findKthLargest(self, nums, k):
        high = 100000
        for i in range(len(nums)):
            tmp = -100000
            for j in range(0, len(nums)):
                if tmp < nums[j] < high:
                    tmp = nums[j]
            for j in range(len(nums)):
                if tmp == nums[j]:
                    k -= 1
                    if k == 0:
                        return tmp
            high = tmp


s = KthLargest()
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
