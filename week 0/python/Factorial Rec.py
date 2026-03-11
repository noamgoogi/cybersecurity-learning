def factorial_iterative(n):
    result = 1
    for x in range(n):
        result *= x + 1
    return result


def factorial_recursive(n):
    if n == 1:
        return 1
    return n* factorial_recursive(n-1)

print(factorial_recursive(5))