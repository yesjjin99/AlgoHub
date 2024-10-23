n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0
for i in range(n):
    for j in range(coins[i], m + 1):
        if d[j - coins[i]] != 10001:  # i - k 방법이 존재하는 경우
            d[j] = min(d[j], d[j - coins[i]] + 1)

print(d[m]) if d[m] != 10001 else print(-1)
