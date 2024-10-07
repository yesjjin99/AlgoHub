import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 네트워크 지연 시간이 크거나 같다면 더 이상 먹을 음식이 없으므로 -1 반환
    if sum(food_times) <= k:
        return -1

    hq = []  # 먹는 시간이 작은 음식부터 제거해야 하므로 우선순위 큐 사용
    for i, v in enumerate(food_times):
        heapq.heappush(hq, (v, i + 1))

    total, prev = 0, 0
    length = len(food_times)

    # [이전 음식 섭취까지 소요한 전체 시간 + 현재 음식을 섭취하기 위해 필요한 시간]이 K보다 커지면, 반복문 종료
    # 현재 음식을 섭취하기 위한 시간은, (현재 음식 섭취 시간 - 이전 음식 섭취 시간) * 남은 음식 개수
    while (total + (hq[0][0] - prev) * length) <= k:
        time = heapq.heappop(hq)[0]
        total += (time - prev) * length
        length -= 1
        prev = time

    # 반복문 종료 이후에는, K 발생까지 남은 시간을 확인해, K 이후에 섭취할 음식을 결정

    # 우선순위큐의 남아있는 요소들을 음식 번호를 기준으로 오름차순 정렬
    hq.sort(key=lambda x: x[1])

    return hq[(k - total) % length][1]  # K 발생까지 남은 시간 % 남은 음식 개수
