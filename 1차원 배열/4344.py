import sys

test_num = int(sys.stdin.readline())
for i in range(test_num):
    test = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for j in test[1:]:
        avg = sum(test[1:]) / test[0]
        if j > avg:
            cnt += 1
    print(f'{cnt / test[0] * 100 :.3f}%')
