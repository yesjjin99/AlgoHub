import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]  # 보석의 정보: 무게, 가격
bags = [int(input()) for _ in range(k)]  # 가방에 담을 수 있는 최대 무게

info.sort()  # 보석, 가방 오름차순 정렬
bags.sort()

total = 0
tmp_jew = []  # 각 가방에 담을 수 있는 모든 보석 (최대힙)

# 가장 작은 가방에 담을 수 있는 보석 중 가장 가치가 큰 것부터 (그리디)
for bag in bags:
    while info and bag >= info[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(info)[1])

    if tmp_jew:
        total -= heapq.heappop(tmp_jew)  # 현재 가방에 넣을 수 있는 보석 중 가장 가치가 큰 보석
    elif not info:
        break

print(total)