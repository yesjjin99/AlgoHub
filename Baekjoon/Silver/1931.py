n = int(input())
v = []
for i in range(n):
    a, b = map(int, input().split())
    v.append([b, a])
v.sort()
a = 0; b = 0
for i in range(n):
    if v[i][1] < a: continue
    a = v[i][0]
    b += 1
print(b)
