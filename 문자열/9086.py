import sys

case = int(sys.stdin.readline())
for _ in range(case):
    word = sys.stdin.readline().rstrip()
    tmp_word = word[0] + word[-1]
    print(tmp_word)
