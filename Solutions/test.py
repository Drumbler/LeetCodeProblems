class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        print(len(s) // 2)
        for i in range(len(s) // 2):

            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
        return s


s = Solution()
print(s.reverseString([1, 2, 3, 4, 5, 6, 7]))
