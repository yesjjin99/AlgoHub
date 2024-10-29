from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

result = bisect_right(arr, x) - bisect_left(arr, x)
print(result) if result > 0 else print(-1)

# ---

def first():
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif arr[mid] >= x:
            end = mid - 1
        else:
            start = mid + 1
    return None

def last():
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
        if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1

def count():
    f, l = first(), last()
    if f is None or l is None:
        return 0
    return l - f + 1

a, b = first(), last()
if a is None:
    print(-1)
else:
    answer = b - a + 1
    print(-1) if answer == 0 else print(answer)
