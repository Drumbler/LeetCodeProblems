class megreStringAlternatelt(object):
    def mergeAlternately(self, word1, word2):
        res = ''
        if len(word1) > len(word2):
            l = len(word1)
        else:
            l = len(word2)
        for i in range(l):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return res


s = megreStringAlternatelt()
print(s.mergeAlternately('abcddd', 'pqr'))
