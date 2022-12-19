index = int(input())

num = 0
num_count = 0

while num_count < index:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    x = index - num_count
    y = num - x + 1
else:
    x = num - (index - num_count) + 1
    y = index - num_count

print(f"{x}/{y}")