def binary_search(arr, target, lenth, start, end):
  answer = 0
  while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in range(lenth):
      if arr[i] > mid:
        sum += (arr[i] - mid)
    
    if sum < target:
      end = mid - 1
    else: # 적어도 m만큼
      answer = mid
      start = mid + 1
  return answer

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = binary_search(arr, m, n, 0, arr[n-1])
print(answer)
