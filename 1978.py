import sys


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
#약수의 대칭성으로 시간복잡도 줄이기

case = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
result = 0
for j in range(len(num_list)):
    if isPrime(num_list[j]):
        result += 1

print(result)
