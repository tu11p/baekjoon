import sys

case = int(sys.stdin.readline())
for i in range(case):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    people = [i for i in range(1, room+1)]
    for j in range(1, floor + 1):
        for k in range(1, room):
            people[k] += people[k - 1]
    print(people[room - 1])

    # 1 2     3       4         5 ...
    # 1 1+2   1+2+3   1+2+3+4   1+2+3+4+5
    # 1 1+3   1+3+6   1+3+6+10

