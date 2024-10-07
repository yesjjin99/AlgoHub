now = input()
x, y = ord(now[0]) - ord('a'), int(now[1]) - 1
count = 0

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

for i in range(len(dx)):
    nx, ny = x + dx[i], y + dy[i],
    if 0 <= nx < 8 and 0 <= ny < 8:
        count += 1

print(count)
