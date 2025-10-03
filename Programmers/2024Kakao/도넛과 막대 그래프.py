def solution(edges):
    MAX_VALUE = 1000001

    answer = [0, 0, 0, 0]
    com = [0] * MAX_VALUE  # 들어오는 간선의 개수
    out = [0] * MAX_VALUE  # 나가는 간선의 개수
    m = 0

    for a, b in edges:
        out[a] += 1
        com[b] += 1
        m = max(m, a, b)

    for i in range(1, m + 1):
        if com[i] == 0 and out[i] >= 2:  # 새로 생성된 정점 : 들어오는 간선 0, 나가는 간선 2 이상
            answer[0] = i
        elif com[i] >= 1 and out[i] == 0:  # 막대 모양 그래프 : 들어오는 간선 1 이상(생성된 정점 포함), 나가는 간선 0
            answer[2] += 1
        elif com[i] >= 2 and out[i] == 2:  # 8자 모양 그래프 : 들어오는 간선 2 이상, 나가는 간선 2 (정 가운데 정점)
            answer[3] += 1

    answer[1] = out[answer[0]] - (answer[2] + answer[3])  # 막대 모양, 8자 모양 그래프를 제외한 나머지가 도넛 모양 그래프

    return answer