class SearchInsertPosition(object):
    def searchInsert(self, nums: list[int], target: int):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        if r == mid:
            return mid + 1
        else:
            return mid



s = SearchInsertPosition()
print(s.searchInsert([1, 3, 5, 6], 4))
