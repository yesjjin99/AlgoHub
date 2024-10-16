import heapq
import sys
input = sys.stdin.readline

n = int(input())
total = 0
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    total += a + b
    heapq.heappush(heap, a + b)

print(total)
