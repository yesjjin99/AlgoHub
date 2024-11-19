def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            a, b = i, yellow // i
            if (a + 2) * (b + 2) == brown + yellow:
                return [b + 2, a + 2]
