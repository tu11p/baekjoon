import sys

'''
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
'''
n = int(sys.stdin.readline())

if n == 1:
    print()
else:
    i = 2
    while n != 1:
        if n % i == 0:
            print(i)
            n = int(n / i)
        else:
            i += 1
