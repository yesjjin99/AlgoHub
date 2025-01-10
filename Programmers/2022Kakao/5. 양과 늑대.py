def solution(info, edges):
    answer = []
    visited = [0] * len(info)

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)  # 양이 늑대보다 많으면 양의 수를 결과 배열에 저장
        else:
            return  # 양이 늑대보다 같거나 적으면 해당 과정을 끝내기

        for a, b in edges:  # 루트노드에서부터 매번 탐색하며 -> 이전 노드로 돌아가 다른 경로까지 갈 수 있도록
            if visited[a] and not visited[b]:  # 부모 노드는 방문했지만, 자식 노드는 방문하지 않은 경우
                visited[b] = 1

                if info[b] == 0:  # 양이라면
                    dfs(sheep + 1, wolf)
                else:  # 늑대라면
                    dfs(sheep, wolf + 1)

                visited[b] = 0  # 백트래킹

    visited[0] = 1
    dfs(1, 0)

    return max(answer)