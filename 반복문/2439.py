import sys
line_num = int(sys.stdin.readline())
for i in range(1, line_num+1):
    print(" " * (line_num-i),end="")
    print("*" * i)