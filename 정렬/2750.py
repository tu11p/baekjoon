import sys

case = int(sys.stdin.readline())
list_num = []

for i in range(case):
    list_num.append(int(sys.stdin.readline()))

for i in range(len(list_num)):
    for j in range(len(list_num)):
        if list_num[i] < list_num[j]:
            list_num[i], list_num[j] = list_num[j], list_num[i]

for n in list_num:
    print(n)
