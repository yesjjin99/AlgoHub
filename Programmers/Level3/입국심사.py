def solution(n, times):
    times.sort()

    start, end = 1, times[-1] * n  # 소요될 수 있는 가장 최소 시간, 가장 최대 시간
    while start <= end:  # n 명의 사람을 심사하는 데 부족하지도, 많지도 않은 가장 적절한 시간 찾기 -> 이진탐색 사용
        mid = (start + end) // 2
        total = 0

        for time in times:
            total += mid // time  # mid 시간 동안 총 몇 명의 사람을 받을 수 있는지

        if total >= n:  # 만약 n 명보다 초과하여 심사했다면 -> 시간이 너무 많은 것
            end = mid - 1
        else:  # 만약 n 명보다 적게 심사했다면 -> 시간이 부족한 것
            start = mid + 1

    return start  # 최소값 반환
