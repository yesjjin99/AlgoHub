from collections import deque

def solution(prices):  # queue로 해야 통과, stack으로 하면 시간초과
    answer = []
    prices = deque(prices)

    while prices:
        p = prices.popleft()
        total = 0
        for i, v in enumerate(prices):
            total += 1
            if p > v:
                break
        answer.append(total)
    return answer


def solution(prices):
    stack = []
    answer = [0] * len(prices)

    for i in range(len(prices)):
        while stack and stack[-1][1] > prices[i]:  # 갸격이 떨어진 경우
            past, _ = stack.pop()
            answer[past] = i - past  # 몇 초만큼 가격이 떨어지지 않았는지
        stack.append([i, prices[i]])

    for i, v in stack:  # 가격이 떨어진 경우를 제외하고(위에서 계산) 몇 초 동안 유지했는지 나머지 계산
        answer[i] = len(prices) - i - 1

    return answer
