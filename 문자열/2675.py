import sys

case_num = int(sys.stdin.readline())

for i in range(case_num):
    split=sys.stdin.readline().split()
    loop_num=int(split[0])
    test_word = split[1]
    for j in str(test_word):
        print(f'{j * int(loop_num)}', end="")
    print()
