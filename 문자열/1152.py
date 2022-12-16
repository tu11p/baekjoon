test_string = input()
if test_string == " ":
    print(0)
else:
    test_string = test_string.strip()
    print(test_string.count(" ") + 1)
