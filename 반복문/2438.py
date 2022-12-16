import sys
line_num = int(sys.stdin.readline())

'''
for i in range(0, line_num):
    for j in range(0, i+1):
        print("*", end='')
    print()
'''

for i in range(1, line_num+1):
    print("*" * i)