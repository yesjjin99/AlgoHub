import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = sum(arr[:k])
answer = s
left, right = 0, k - 1  # 투 포인터

while right < n - 1:
    s = s - arr[left] + arr[right + 1]
    answer = max(answer, s)
    left += 1
    right += 1

print(answer)