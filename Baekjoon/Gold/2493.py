n = int(input())
heights = list(map(int, input().split()))
answer = [0] * n

stack = []
for i in range(n):
    while stack:
        if stack[-1][1] >= heights[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()

    stack.append((i, heights[i]))

print(*answer)