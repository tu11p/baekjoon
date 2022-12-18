import sys

test_num = int(sys.stdin.readline())
result = test_num
for i in range(test_num):
    test_word = sys.stdin.readline()
    for j in range(len(test_word) - 1):
        if test_word[j] != test_word[j + 1]:
            if test_word[j] in test_word[j + 1:]:
                result -= 1
                break
print(result)
