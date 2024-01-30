class longestPrefix(object):
    def longestCommonPrefix(self, strs):
        # res = ''
        # strs = sorted(strs)
        # first = strs[0]
        # last = strs[-1]
        # for i in range(min(len(first), len(last))):
        #     if first[i] != last[i]:
        #         return res
        #     res += first[i]
        # return res

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[0][i] != strs[j][i]:
                    return strs[0][0:i] if i > 0 else ''
        return strs[0]


s = longestPrefix()
print(s.longestCommonPrefix(["ab", "a"]))
