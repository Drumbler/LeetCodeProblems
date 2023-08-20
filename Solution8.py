class Solution8(object):
    def maxProfit(self, prices):
        diff = 0
        m = 1000000
        for i in range(0, len(prices)):
            diff = max(prices[i] - m, diff)
            m = min(prices[i], m)
        return diff


s = Solution8()
print(s.maxProfit([7, 4, 5, 3, 6, 1]))
