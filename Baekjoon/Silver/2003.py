N, M = map(int, input().split())
L = list(map(int, input().split()))
ans = 0; left = 0; right = 0; S = 0
while 1:
    if S >= M:
        S -= L[left]
        left += 1
    elif right == N: break
    else:
        S += L[right]
        right += 1
    if S == M: ans += 1
print(ans)
