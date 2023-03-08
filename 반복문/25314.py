import sys

n = int(sys.stdin.readline())
typ = n // 4

while typ != 0:
    print("long", end=" ")
    typ -= 1

print("int")
