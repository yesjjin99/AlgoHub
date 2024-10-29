n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
start, end = 0, arr[-1]

result = 0
# 탐색 범위가 크므로 이진탐색 사용!
while start <= end:
    mid = (start + end) // 2  # 절단기 높이 설정
    total = 0
    for i in arr:
        if i > mid:
            total += i - mid

    if total == m:
        result = mid
        break
    elif total < m:
        end = mid - 1
    else:
        start = mid + 1

print(result)
