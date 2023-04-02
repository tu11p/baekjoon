import sys

basket_num, swap_range = map(int, sys.stdin.readline().split())
basket_list = list(range(1, basket_num + 1))

for _ in range(swap_range):
    begin, end, mid = map(int, sys.stdin.readline().split())
    basket_list = basket_list[:begin - 1] + basket_list[mid - 1:end] + basket_list[begin - 1:mid - 1] + basket_list[end:]

print(*basket_list)
