answer = 0

def solution(k, dungeons):
    visited = [0] * len(dungeons)

    def dfs(k, visited, cnt):
        global answer
        for i, d in enumerate(dungeons):
            answer = max(answer, cnt)

            if k >= d[0] and not visited[i]:
                visited[i] = 1
                dfs(k - d[1], visited, cnt + 1)
                visited[i] = 0  # 백트래킹

    dfs(k, visited, 0)
    return answer
