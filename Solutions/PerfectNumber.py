def get_divisors(num):
    if num == 1:
        return
    yield 1
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            yield i
            yield num // i


def check_perfect_number(num):
    return sum(get_divisors(num)) == num


print(check_perfect_number(0))
