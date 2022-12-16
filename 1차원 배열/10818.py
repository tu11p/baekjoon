import sys
cnt = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
max=num_list[0]
min=num_list[0]
for i in range(0, cnt):
    if num_list[i]>max:
        max=num_list[i]
    if num_list[i]<min:
        min=num_list[i]
print(f'{min} {max}')