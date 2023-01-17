import sys


def factorial(n):
    while n > 0:
        return n * factorial(n - 1)
    return 1


case = int(sys.stdin.readline())
print(factorial(case))
