def firstUniqChar(s: str) -> int:
    count = dict.fromkeys(s, 0)
    for i in s:
        count[i] += 1
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
    return -1


print(firstUniqChar('leetcode'))
