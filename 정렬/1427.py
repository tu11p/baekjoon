import sys

num = int(sys.stdin.readline())
list_num = []
n = 0

for i in str(num):
    list_num.append(int(i))
    n += 1

list_num.sort(reverse=True)
num_result = 0
for j in range(n):
    num_result += list_num[j] * 10 ** (n - j-1)
print(num_result)
