def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if arr[mid] == target:
      return True
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return False

n = int(input())
n_arr = list(map(int, input().split()))
n_arr.sort() # 이진 탐색 위해 정렬
m = int(input())
m_arr = list(map(int, input().split()))

for i in range(len(m_arr)):
  success = binary_search(n_arr, m_arr[i], 0, n - 1)
  if success:
    print("yes", end=" ")
  else:
    print("no", end=" ")
