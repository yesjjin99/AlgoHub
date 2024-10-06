def solution(routes):
    answer = 0
    routes.sort()  # 출발시간으로 정렬

    while routes:
        cam = min(map(lambda x: x[1], routes))  # 도착시간 중 최소값을 카메라 위치로 설정
        while routes and routes[0][0] <= cam <= routes[0][1]:
            routes.pop(0)
        answer += 1

    return answer


def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30001
    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer
