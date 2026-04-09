import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

dp = [[0, 1] for _ in range(n + 1)]  # [정점 번호][얼리어답터 여부]
# 얼리어답터 여부에서 0번 인덱스는 자신이 얼리어답터가 아닌 케이스, 1번 인덱스는 자신이 얼리어답터인 케이스

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Tree DP
def dfs(start):  # 트리 전체 순회
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            dp[start][0] += dp[i][1]  # 본인이 얼리어답터가 아닌 경우 = 자식 노드가(서브트리) 얼리어답터일 때의 최적해를 더해준다
            dp[start][1] += min(dp[i][0], dp[i][1])  # 본인이 얼리어답터인 경우 = 자식 노드가(서브트리) 얼리어답터여도 되고 아니어도 됨 -> 그 중 최소값을 더해준다

dfs(1)
print(min(dp[1]))