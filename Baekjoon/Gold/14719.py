h, w = map(int, input().split())  # 세로 길이, 가로 길이
blocks = list(map(int, input().split()))
answer = 0

for i in range(1, w - 1):
    left = max(blocks[:i])
    right = max(blocks[i + 1:])
    t = min(left, right)

    if blocks[i] < t:
        answer += t - blocks[i]

print(answer)