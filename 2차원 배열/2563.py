import sys

arr = [[0 for _ in range(101)] for _ in range(101)]
case = int(sys.stdin.readline())

for _ in range(case):
    x, y = map(int, sys.stdin.readline().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1

result = 0

for i in arr:
    result += i.count(1)

print(result)
