n = int(input())
n *= 2
v = list(map(int, input().split()))
v.sort()
a = 1234567891
for i in range(n):
    a = min(a, v[i] + v[n-1-i])
print(a)
