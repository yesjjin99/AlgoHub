from itertools import combinations

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

answer = int(1e9)
com = list(combinations(range(n), n // 2))
for i in range(len(com) // 2):
    team1, team2 = 0, 0
    for a, b in combinations(com[i], 2):
        team1 += s[a][b] + s[b][a]
    for a, b in combinations(com[len(com) - i - 1], 2):
        team2 += s[a][b] + s[b][a]

    answer = min(answer, abs(team1 - team2))

print(answer)

# ---

answer = int(1e9)
visited = [False] * n  # 0이면 스타크팀, 1이면 링크팀

def dfs(cnt, idx):
    global answer

    if cnt == (n // 2):
        t1, t2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    t1 += s[i][j]
                elif not visited[i] and not visited[j]:
                    t2 += s[i][j]

        answer = min(answer, abs(t1 - t2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, i + 1)
            visited[i] = False  # 백트래킹

dfs(0, 0)
print(answer)
