answer = 0

def dfs(numbers, target, i, result):
    global answer
    if i == len(numbers):
        if result == target:
            answer += 1
        return
    dfs(numbers, target, i + 1, result + numbers[i])
    dfs(numbers, target, i + 1, result - numbers[i])

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer


def solution(numbers, target):
    if not numbers:
        return 1 if target == 0 else 0
    else:
        # target 을 초기값으로 잡고 numbers 를 줄여가며 재귀 호출
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])


from itertools import product

def solution(numbers, target):
    l = [(-x, x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
