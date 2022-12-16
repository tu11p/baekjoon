def self_num():
    num = set(range(1, 10001))
    not_self_num = set()
    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        not_self_num.add(i)

    return sorted(num - not_self_num)


tmp = self_num()
for k in tmp:
    print(k)
