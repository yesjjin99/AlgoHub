n = int(input())
arr = list(map(int, input().split()))
start, end = 0, n - 1

answer = -1
while start <= end:
    mid = (start + end) // 2
    if mid == arr[mid]:
        answer = mid
        break
    elif mid < arr[mid]:
        end = mid - 1
    else:
        start = mid + 1

print(answer)
