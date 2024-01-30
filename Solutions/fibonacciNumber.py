class fibonacciNumber(object):
    def fib(self, n):
        prev = 0
        curr = 1
        res = 0
        if n == 1:
            return 1
        for i in range(n - 1):
            res = prev + curr
            prev = curr
            curr = res
        return res


s = fibonacciNumber()
print(s.fib(1))
