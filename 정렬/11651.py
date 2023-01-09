import sys

case = int(sys.stdin.readline())
list_crd = [[0 for col in range(2)] for row in range(case)]
a = 0
b = 0

for i in range(case):
    a, b = map(int, sys.stdin.readline().split())
    list_crd[i][0] = a
    list_crd[i][1] = b

list_crd.sort(key=lambda x: (x[1], x[0]))  # 먼저 1번 인덱스에 대해서 정렬하고 0번 인덱스에 대해서 정렬

for j in range(case):
    print(list_crd[j][0], list_crd[j][1])
