class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        n = x[::-1]
        if x == n:
            return "true"
        else:
            return "false"


s = Solution()
print(s.isPalindrome(-121))
