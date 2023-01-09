import sys

case = int(sys.stdin.readline())

list_word = []

for i in range(case):
    list_word.append(sys.stdin.readline().strip())

list_word = list(set(list_word))
list_word.sort()
list_word.sort(key=lambda x: len(x))

for j in list_word:
    print(j)
