import sys
test_num=int(sys.stdin.readline())

for i in range(0,test_num):
    a, b = map(int, sys.stdin.readline().split())
    print(f'{a+b}')