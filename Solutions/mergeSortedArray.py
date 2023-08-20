class mergeSortedArray(object):
    def merge(self, nums1, m, nums2, n):
        for v in range(m - 1, len(nums1)):
            if nums1[v] == 0:
                nums1[v] = nums2[v - m]
        nums1.sort()
        return nums1


s = mergeSortedArray()
print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
