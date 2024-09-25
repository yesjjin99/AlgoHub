from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer, s = 0, 0
    bridge = deque([0] * bridge_length)

    while truck_weights:
        s -= bridge.popleft()
        if s + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            s += truck
        else:
            bridge.append(0)
        answer += 1
    return answer + bridge_length  # 마지막 트럭이 다리를 모두 건널 때까지 카운트
