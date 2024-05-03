class SummaryRanges:
    def summaryRanges(nums):
        count = 0
        start = 0
        res = []
        for i, n in enumerate(nums):
            if n == 0:
                res.append("0")
                start = nums[i+1]
            if (n - 1) != nums[i - 1] and n != 0:
                res.append(f"{start}->{nums[i - 1]}")
                start = n
        print(res)


s = SummaryRanges
print(s.summaryRanges([0, 1, 3, 4, 6]))
