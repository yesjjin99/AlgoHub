s = list(map(int, input()))
ans = 0

for n in s:
    ans = max(ans + n, ans * n)

print(ans)