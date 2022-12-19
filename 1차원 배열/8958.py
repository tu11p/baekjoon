import sys

test_num = int(sys.stdin.readline())
for i in range(test_num):
    score = 0
    tmp_score = 0
    test = sys.stdin.readline()
    for j in test:
        if j == 'O':
            tmp_score = tmp_score + 1
        else:
            tmp_score = 0
        score = score + tmp_score
    print(score)
