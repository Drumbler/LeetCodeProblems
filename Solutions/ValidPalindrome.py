import string


class ValidPalindrome(object):
    def isPalindrome(self, s: str) -> bool:
        # table = str.maketrans("", "", string.punctuation)
        # s = s.translate(table).lower().replace(' ', '')
        # print(s)
        # return s == s[::-1]

        # ---------------------

        # charsToDel = [' ', ':', ';', ',', '.', '/', '?',
        #               '!', '|', '@', '#', '$', '%', '^',
        #               '&', '*', '(', ')', '_', '+', '[',
        #               ']', '{', '}', '"', '\\', "'", '-', '=', '`']
        # for c in s:
        #     if c in charsToDel:
        #         s = s.replace(c, '')
        # s = s.lower()
        # return s == s[::-1]

        # ---------------------
        l = 0
        r = len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if l >= r:
                return True
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


s = ValidPalindrome()
# print(s.isPalindrome('A man, a plan, a canal: Panama'))
print(s.isPalindrome(','))
