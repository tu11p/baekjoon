import sys

test_num, award_num = map(int, sys.stdin.readline().split())
list_score = list(map(int, sys.stdin.readline().split()))

for i in range(len(list_score)):
    for j in range(len(list_score)):
        if list_score[i] < list_score[j]:
            list_score[i], list_score[j] = list_score[j], list_score[i]

print(list_score[len(list_score) - award_num])
