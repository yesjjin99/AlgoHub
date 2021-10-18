n, k = map(int, input().split())
result = 0

while True:
  # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
  target = (n // k) * k
  result += (n - target) # 1씩 빼야하는 경우 한번에 계산해줌
  if n < k:
    break
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
