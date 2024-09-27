from functools import cmp_to_key

def solution(numbers):
    numbers = sorted(numbers, key=cmp_to_key(comp))
    return str(int("".join(map(str, numbers))))

def comp(x, y):
    if str(x) + str(y) < str(y) + str(x): return 1
    else: return -1
