import sys

test_case = int(sys.stdin.readline())
test_num = int(sys.stdin.readline())
test_sum = 0
for i in str(test_num):
    test_sum = test_sum + int(i)

print(test_sum)
