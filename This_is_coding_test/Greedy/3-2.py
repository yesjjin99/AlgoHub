n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
a, b = nums[0], nums[1],

if a == b:
    print(a * m)
else:
    print(a * k * (m // k) + b * (m % k))
