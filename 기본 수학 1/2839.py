import sys

n = int(sys.stdin.readline())
if n % 5 == 0:
    print(n // 5)
else:
    result = 0
    while n >= 0:
        if n % 5 == 0:
            result += (n // 5)
            print(result)
            break
        n -= 3
        result += 1
    else:
        print(-1)
