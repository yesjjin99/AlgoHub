N, M = map(int, input().split())
num = list(map(int, input().split()))
high = max(num)
low = 0

ans = -1
while high >= low:
    mid = (high + low)//2
    S = 0
    for i in range(N):
        if num[i] - mid > 0:
            S += num[i] - mid
    if S < M:
        high = mid - 1
    else:
        ans = max(ans, mid)
        low = mid + 1
print(ans)
