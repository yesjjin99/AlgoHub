from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1  # 점검이 불가능한 경우 가정
    len_weak = len(weak)

    for i in range(len_weak):  # 길이를 2배로 늘리면 방향을 고려할 필요 없음 (원형을 평면으로 펼치기)
        weak.append(weak[i] + n)

    for start in range(len_weak):  # 취약 지점에서 출발
        for friends in list(permutations(dist, len(dist))):  # 경우의 수 각각에 대하여
            count = 1  # 점검 인원 1명으로 시작
            arrival = weak[start] + friends[count - 1]  # 도착 지점 = 출발 지점 + 친구가 이동한 가능한 최대 거리

            for point in range(start, start + len_weak):  # 출발 지점에서부터 하나씩 모든 지점을 살펴보며
                if arrival < weak[point]:  # 최대 가능 거리를 갔음에도 여전히 점검할 지점이 남아있는 경우
                    count += 1  # 친구 1명 더 투입
                    if count > len(dist):  # 더이상 투입할 친구가 없는 경우, break
                        break

                    arrival = weak[point] + friends[count - 1]  # 새로운 친구의 도착 지점 갱신

            answer = min(answer, count)

    if answer > len(dist):  # 필요한 친구 수가 주어진 친구 수보다 많을 경우, -1 반환
        return -1
    return answer
