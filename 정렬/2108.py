import sys
from collections import Counter

case = int(sys.stdin.readline())

list_num = []

for i in range(case):
    list_num.append(int(sys.stdin.readline()))

list_num.sort()

# 산술평균
print(int(round(sum(list_num) / case, 0)))  # round: 반올림

# 중앙값
print(list_num[case // 2])

# 최빈값
tuple_num = Counter(list_num).most_common()

if len(list_num) > 1:  # 입력값이 1개일 경우 예외
    if tuple_num[0][1] == tuple_num[1][1]:
        print(tuple_num[1][0])
    else:
        print(tuple_num[0][0])
else:
    print(list_num[0])

# 범위
print(list_num[-1] - list_num[0])
