class BinarySearch(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        mid = right // 2
        while nums[mid] != target and left <= right:
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2
        if left > right:
            return -1
        else:
            return mid


s = BinarySearch()
print(s.search([1, 2, 3, 4], 5))
