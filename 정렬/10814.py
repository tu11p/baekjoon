import sys

case = int(sys.stdin.readline())

arr = [[0 for col in range(2)] for row in range(case)]
a = 0
b = 0

for i in range(case):
    a, b = sys.stdin.readline().split()
    arr[i][0] = int(a)
    arr[i][1] = b

arr.sort(key=lambda x: x[0])

for j in range(case):
    print(arr[j][0], arr[j][1])
