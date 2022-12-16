import sys
import copy
num = []
for i in range(0, 9):
    a = int(sys.stdin.readline())
    num.insert(i, a)
'tmp = copy.deepcopy(num)' #Shallow copy
tmp = num.copy() #deep copy
## 이 문제는 둘다 되는듯
num.sort()
print(num[8])
print(tmp.index(num[8])+1)
