class findIndex(object):
    def strStr(self, haystack, needle):
        # return(haystack.find(needle, 0, len(haystack)))
        ##############################
        # if needle in haystack:
        #     return  haystack.index(needle)
        # else:
        #     return -1
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1


s = findIndex()
print(s.strStr('leetcode', 'leet1'))
