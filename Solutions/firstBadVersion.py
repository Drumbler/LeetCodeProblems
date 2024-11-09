import bisect


def firstBadVersion(n: int) -> int:
    data = [num for num in range(1, n+1)]
    l = 0
    r = n

    while l < r:
        mid = (l + r) // 2
        if isBadVersion(data[mid]) == False:
            l = mid
        elif isBadVersion(data[mid]) == True:
            r = mid + 1
        else:
            return mid
    return -1


print()
