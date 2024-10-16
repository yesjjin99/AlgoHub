import sys
input = sys.stdin.readline

n = int(input())
students = []
for _ in range(n):
    students.append(input().split())

students.sort(key=lambda s: (-int(s[1]), int(s[2]), -int(s[3]), s[0]))

for s in students:
    print(s[0])
