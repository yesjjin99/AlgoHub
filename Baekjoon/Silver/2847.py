n = int(input())
v = []
for i in range(n):
    v.append(int(input()))

ans = 0
for i in range(n-2, -1, -1):
    if v[i+1] <= v[i]:
        ans += v[i] - (v[i+1] - 1)
    v[i] = min(v[i], v[i+1] - 1)
print(ans)
