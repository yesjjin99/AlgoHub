INF = int(1e9)

n = int(input())
arr = sorted(list(map(int, input().split())))

left, right = 0, n - 1  # 투 포인터
answer = [INF, INF]
while left < right:  # left와 right가 만나면 종료
    s = arr[left] + arr[right]

    if abs(s) < abs(sum(answer)):
        answer = [arr[left], arr[right]]
        if s == 0:
            break

    if s < 0:
        left += 1
    else:
        right -= 1

print(*answer)