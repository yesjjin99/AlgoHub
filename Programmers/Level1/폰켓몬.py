from collections import Counter

def solution(nums):
    c = Counter(nums)
    return min(len(nums) // 2, len(c))


def solution(nums):
    return min(len(nums) // 2, len(set(nums)))
