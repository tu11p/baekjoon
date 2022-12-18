import sys

cnt = 1
result = 1
dest = int(sys.stdin.readline())
if dest == 1:
    print(1)
else:
    while dest > cnt:
        cnt += result * 6
        result += 1

    print(result)
