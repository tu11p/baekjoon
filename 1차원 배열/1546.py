import sys
test_num = int(sys.stdin.readline())
test_result = list(map(int, sys.stdin.readline().split()))
print(f'{(sum(test_result) / test_num) / max(test_result) * 100}')
