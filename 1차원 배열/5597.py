student = [i for i in range(1, 31)]

for j in range(1,29):
    num = int(input())
    student.remove(num)

print(min(student))
print(max(student))
