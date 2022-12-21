import sys


# 에라토스테네스의 체
def prime_list(n):
    all_prime = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if all_prime[i] == True:
            for j in range(i + i, n, i):
                all_prime[j] = False
    return [i for i in range(2, n) if all_prime[i] == True]


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    count = 0
    prime_list = [True] * (2 * n + 1)
    for i in range(2, int((n * 2) ** 0.5) + 1):
        if prime_list[i]:
            for j in range(i + i, n * 2 + 1, i):
                prime_list[j] = False

    for x in range(n + 1, 2 * n + 1):
        if prime_list[x]:
            count += 1

    print(count)
