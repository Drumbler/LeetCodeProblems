import math


class pascalsTriangle(object):
    def generate(self, numRows):
        triangle = []
        for i in range(0, numRows):
            if i == 0:
                curr = [1]
            elif i == 1:
                curr = [1, 1]
            else:
                # curr = [prev[j] + prev[j + 1] for j in range(len(curr) - 1)]
                curr = [sum(x) for x in zip(prev, prev[1:])]
                curr = [1] + curr + [1]

            triangle.append(curr)
            prev = curr
        return triangle[numRows-1]


s = pascalsTriangle()
print(s.generate(4))
