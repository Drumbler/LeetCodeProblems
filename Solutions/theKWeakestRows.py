def kWeakestRows(mat, k):
    result = [i for i in range(len(mat))]
    count = 1
    while count < len(mat):
        for i in range(len(mat) - count):
            if mat[i].count(1) > mat[i + 1].count(1):
                mat[i], mat[i + 1] = mat[i + 1], mat[i]
                result[i], result[i + 1] = result[i + 1], result[i]
        count += 1
    return result[:k:1]


print(kWeakestRows([[1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1]], 3))
