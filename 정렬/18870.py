import sys, bisect

case = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = sorted(list(set(arr1)))

for i in range(case):
    print(bisect.bisect_left(arr2, arr1[i]), end=" ") #이진탐색으로 시간복잡도 줄이기
