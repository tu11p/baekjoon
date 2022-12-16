num = int(input())
cycle = 0
new_num = 10 * (num % 10) + (int(num / 10) + num % 10) % 10
cycle = cycle + 1
while num != new_num:
    new_num = 10 * (new_num % 10) + (int(new_num / 10) + new_num % 10) % 10
    cycle = cycle + 1
print(cycle)
'''
if num < 10:
    new_num = num * 11
elif int(num / 10) + (num % 10) < 10:
    new_num = int(num / 10) + (num % 10) * 11
elif (int(num / 10) + (num % 10)) % 10 == 0:
    new_num = num % 10 * 10
else:
    new_num = (num % 10) * 10 + (int(num / 10) + int((num % 10) / 10))
cycle = cycle + 1
while 1:
    if (cycle == 1) & (new_num == 0):
        break
    if (new_num > 0) & (new_num < 10):
        new_num = new_num * 11
    elif (int(new_num / 10) + (new_num % 10)) >= 10:
        new_num = 10 * (new_num % 10) + int(new_num / 10) + (new_num % 10) - 10
    else:
        new_num = 10 * (new_num % 10) + int(new_num / 10) + (new_num % 10)
    if num == new_num:
        cycle = cycle + 1
        break
    cycle = cycle + 1
print(cycle)
'''
