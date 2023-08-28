class climbingStairs(object):
    def climbStairs(self, n):
        prev1 = 1
        prev2 = 1
        curr = 0
        if n <= 1:
            return 1
        for i in range(1, n):
            curr = prev1 + prev2
            prev2, prev1 = prev1, curr
        return curr


s = climbingStairs()
print(s.climbStairs(4))
