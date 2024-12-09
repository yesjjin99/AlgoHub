import math

def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1):  # 원의 방정식 활용
        if i < r1:
            s = math.ceil(math.sqrt(r1 ** 2 - i ** 2))
        else:  # i값이 r1보다 크거나 같으면 항상 시작은 0
            s = 0

        e = int(math.sqrt(r2 ** 2 - i ** 2))
        answer += e - s + 1  # 범위 사이의 개수 모두 더하기

    return answer * 4  # 시간복잡도 고려해서 1사분면만 구하고 *4 (O(n))
