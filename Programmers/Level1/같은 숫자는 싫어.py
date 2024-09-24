def solution(arr):
    stack = [arr[0]]
    for i in range(1, len(arr)):
        if stack[-1] != arr[i]:
            stack.append(arr[i])
    return stack


def solution(arr):
    stack = []
    for n in arr:
        if len(stack) == 0 or stack[-1] != n:
            stack.append(n)
    return stack
