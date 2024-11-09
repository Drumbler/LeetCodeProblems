from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if len(strs[j]) <= i or strs[0][i] != strs[j][i]:
                return strs[0][0:i] if i > 0 else ''
    return strs[0]
