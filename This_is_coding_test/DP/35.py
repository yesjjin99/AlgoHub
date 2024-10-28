n = int(input())
dp = [0] * 1001
cnt, answer = 1, 0

dp[1] = 1
for i in range(2, 1001):
    if n == 1:
        answer = 1
        break

    if i % 2 == 0 and dp[i // 2] == 1:
        dp[i] = 1
        cnt += 1
    elif i % 3 == 0 and dp[i // 3] == 1:
        dp[i] = 1
        cnt += 1
    elif i % 5 == 0 and dp[i // 5] == 1:
        dp[i] = 1
        cnt += 1

    if cnt == n:
        answer = i
        break

print(answer)
