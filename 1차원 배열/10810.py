import sys

n, m = map(int, sys.stdin.readline().split())
basket = [0 for a in range(n)]
for b in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for index in range(i, j+1):
        basket[index-1]=k
for i in range(n):
    print(basket[i], end=" ")
