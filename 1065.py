# 한수가 아닌 수 카운트해서 전체에서 빼기
import sys


def han_num(num):
    cnt = 0

    for i in range(1, num + 1):
        if len(str(i)) == 3 and (int(str(i)[2]) - int(str(i)[1])) != (int(str(i)[1]) - int(str(i)[0])):
            cnt += 1
        elif len(str(i)) == 4:
            cnt += 1

    return num - cnt


num = int(sys.stdin.readline())
print(han_num(num))
