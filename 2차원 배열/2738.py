import sys

n, m = map(int, sys.stdin.readline().split())
list_a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
list_b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

list_result = [[list_a[i][j] + list_b[i][j] for j in range(m)] for i in range(n)]

for j in range(n):
    for k in range(m):
        print(list_result[j][k], end=" ")
    print()
