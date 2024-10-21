import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

start, end = 1, house[-1] - house[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    last = house[0]  # 첫 번째 집은 무조건 설치
    for i in range(1, n):  # 지정한 최소 공유기 사이 거리를 기준으로 설치 가능한 공유기의 총 개수 카운트
        if house[i] - last >= mid:  # 현재 탐색하는 집의 위치와 이전에 설치한 집의 거리가 최소 거리보다 크거나 같을 때 설치 가능
            cnt += 1
            last = house[i]

    if cnt >= c:
        start = mid + 1
        answer = mid  # 최적의 결과 저장
    else:
        end = mid - 1

print(answer)
