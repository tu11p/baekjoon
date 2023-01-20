import sys

case = int(sys.stdin.readline())
for i in range(case):
    s = sys.stdin.readline().rstrip()
    count = 0


    def recursion(s, l, r):
        global count
        count += 1
        if l >= r:
            return 1
        elif s[l] != s[r]:
            return 0
        else:
            return recursion(s, l + 1, r - 1)


    def isPalindrome(s):
        return recursion(s, 0, len(s) - 1)


    print(isPalindrome(s), count)
