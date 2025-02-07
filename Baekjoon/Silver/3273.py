n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
result = 0
l, r = 0, n - 1
while l < r:  # 투 포인터
    if nums[l] + nums[r] == x:
        result += 1

    if nums[l] + nums[r] <= x:
        l += 1
    else:
        r -= 1

print(result)