dp = [1] * 10001  # 1의 합으로 숫자를 만드는 방법은 모두 1가지

for i in range(2, 10001):
    dp[i] += dp[i - 2]  # 1, 2의 합으로 숫자를 만드는 방법은 (n - 2)를 1의 합만으로 만든 방법에 2를 더해주면 된다

for i in range(3, 10001):
    dp[i] += dp[i - 3]  # 1, 2, 3의 합으로 만드는 방법은 (n - 3)을 1과 2의 합만으로 만든 방법에 3을 더해주면 된다

for _ in range(int(input())):
    n = int(input())
    print(dp[n])