import sys

num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
max_num = num_list[0][0]
max_col = 1
max_row = 1

for i in range(9):
    for j in range(9):
        if num_list[i][j] > max_num:
            max_num = num_list[i][j]
            max_col = j + 1
            max_row = i + 1

print(max_num)
print(max_row, max_col)
