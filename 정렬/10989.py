# 카운팅 정렬?
import sys

n = int(sys.stdin.readline())
counts = [0] * 10001
for i in range(n):
    counts[int(sys.stdin.readline())] += 1
for input_number in range(1, 10001):
    if counts[input_number] != 0:
        for _ in range(counts[input_number]):
            print(input_number)
