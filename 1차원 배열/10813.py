import sys

n, m = map(int, sys.stdin.readline().split())
basket = [a for a in range(1, n+1)]
for b in range(m):
    i, j = map(int, sys.stdin.readline().split())
    tmp = basket[i - 1]
    basket[i - 1] = basket[j - 1]
    basket[j - 1] = tmp

for c in basket:
    print(c, end=" ")
