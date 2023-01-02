import sys

case = int(sys.stdin.readline())
list_num = []
for _ in range(case):
    list_num.append(int(sys.stdin.readline()))
list_num.sort()
for i in range(case):
    print(list_num[i])