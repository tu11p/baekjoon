import sys

test_num = int(sys.stdin.readline())
for i in range(test_num):
    ho_h, ho_w, guest = map(int, sys.stdin.readline().split())
    # int(guest / ho_h)+1
    # int(guest % ho_h)
    if guest % ho_h == 0:
        print(ho_h * 100 + int(guest / ho_h))
    else:
        print(int(guest % ho_h) * 100 + int(guest / ho_h) + 1)
