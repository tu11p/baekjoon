import sys
num = []
for i in range(10):
    a = int(sys.stdin.readline()) % 42
    num.append(a)
print(len(set(num)))