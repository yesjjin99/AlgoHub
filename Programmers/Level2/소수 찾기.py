from itertools import permutations

def prime_number(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    result = set()

    for i in range(1, len(numbers) + 1):
        for p in set(permutations(numbers, i)):
            num = int("".join(p))
            if prime_number(num):
                result.add(num)

    return len(result)
