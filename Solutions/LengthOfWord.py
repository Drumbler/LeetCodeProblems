class LengthOfWord(object):
    def lengthOfLastWord(self, s):
        # l = len(s) - 1
        # r = len(s) - 1
        # while s[r] == ' ':
        #     r -= 1
        #     l -= 1
        # while s[l] != ' ' and l >= 0:
        #     l -= 1
        # return r - l
#-----------------------------------
        return len(s.rstrip().split(' ')[-1])


s = LengthOfWord()
print(s.lengthOfLastWord('asd wwa '))
