class duplicate(object):
    def containsDuplicate(self, nums):
        #перерешать
        s = set()
        for v in nums:
            nums_dict[v] += 1
            if nums_dict[v] > 1:
                return True
        return False



s = duplicate()
print(s.containsDuplicate([2, 14, 18, 22, 22]))
