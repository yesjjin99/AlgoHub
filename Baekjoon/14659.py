n = int(input())
v = list(map(int, input().split()))
cur_max = 0; ans = 0; a = 0
for i in range(n):
    if cur_max < v[i]:
        cur_max = v[i]
        ans = max(ans, a)
        a = -1
    a += 1

ans = max(ans, a)
print(ans)
