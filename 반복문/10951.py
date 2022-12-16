import sys
while 1:
    try:
        a, b = map(int,sys.stdin.readline().split())
        print(f'{a+b}')
    except EOFError:
        break