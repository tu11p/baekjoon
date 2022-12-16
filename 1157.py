test_word = input().upper()
test_set = list(set(test_word))
test_list = []

for i in test_set:
    test_list.append(test_word.count(i))

if test_list.count(max(test_list)) > 1:
    print("?")
else:
    print(test_set[(test_list.index(max(test_list)))])
