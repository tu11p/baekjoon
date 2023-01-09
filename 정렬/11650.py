import sys

case = int(sys.stdin.readline())
list_crd = [[0 for col in range(2)] for row in range(case)]
x = 0
y = 0

for i in range(case):
    x, y = map(int, sys.stdin.readline().split())
    list_crd[i][0] = x
    list_crd[i][1] = y

list_crd.sort()

for j in range(case):
    print(list_crd[j][0], list_crd[j][1])