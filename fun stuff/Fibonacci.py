def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(37))
# n = 10
# for i in range(n):
#     print(fibonacci(i))
