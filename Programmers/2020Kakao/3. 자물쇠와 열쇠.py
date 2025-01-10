# 자물쇠와 열쇠
def rotate(arr):  # 2차원 리스트 90도 회전
    m = len(arr)
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[j][m - i - 1] = arr[i][j]
    return result

def check(new_lock):  # 자물쇠의 중간 부분이 모두 1인지 확인
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n, m = len(lock), len(key),
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]  # 비교를 위해 자물쇠의 크기를 기존의 3배로 변환
    for i in range(n):  # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):  # 4가지 방향에 대해서 확인
        key = rotate(key)  # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):  # 자물쇠에 열쇠 끼워넣기
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock):  # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                    return True

                for i in range(m):  # 자물쇠에 열쇠 다시 빼기(백트래킹)
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False
