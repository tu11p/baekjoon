import sys

test_word = sys.stdin.readline()
for i in range(97, 123):
    print(test_word.find(chr(i)))