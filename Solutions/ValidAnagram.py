import collections


def isAnagram(s, t) -> bool:
    count = collections.Counter(s)

    for c in t:
        if c not in count:
            return False
        count[c] -= 1
    for v in count.values():
        if v != 0:
            return False
    return True


print(isAnagram('rac', 'car'))
