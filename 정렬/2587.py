import sys

list_num = []
for _ in range(5):
    list_num.append(int(sys.stdin.readline()))
for i in range(5):
    for j in range(5):
        if list_num[i] < list_num[j]:
            list_num[i], list_num[j] = list_num[j], list_num[i]

print(sum(list_num) // 5)
print(list_num[2])