class containsDuplicate:
    def containsNearbyDuplicate(self, nums: list[int], k: int):
        dictionary = {}
        for i, num in enumerate(nums):
            if abs(i - dictionary.get(num, -k-1)) <= k:
                return True
            dictionary[num] = i
        return False


s = containsDuplicate()
print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
