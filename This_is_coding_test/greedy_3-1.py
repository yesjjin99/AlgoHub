# 가장 큰 수 K번 더하고 두 번째로 큰 수 한 번 더하면 됨

n, m, k = map(int, input().split())
# N, M, K를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
  for i in range(k):
    if m == 0: # m이 0이면 반복문 탈출
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)
