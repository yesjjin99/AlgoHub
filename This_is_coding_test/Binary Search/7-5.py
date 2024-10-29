import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
x = list(map(int, input().split()))

def binary_search(target):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in x:
    if binary_search(i) is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# ---

n = int(input())
arr = [0] * 1000001
m = int(input())
x = list(map(int, input().split()))

for i in input().split():  # 계수 정렬
    arr[int(i)] = 1

for i in x:
    if arr[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# ---

n = int(input())
arr = set(map(int, input().split()))  # set 자료구조를 사용하여 중복 제거
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in arr:
        print('yes', end=' ')
    else:
        print('no', end=' ')
