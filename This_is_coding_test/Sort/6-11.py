n = int(input())
students = []
for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x: x[1])

for i in range(n):
    print(students[i][0], end=' ')
