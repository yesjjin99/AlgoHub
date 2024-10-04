n = int(input())
tour = list(map(int, input().split()))
cnt, group = 0, 0

tour.sort()
for t in tour:
    cnt += 1
    if cnt >= t:
        group += 1
        cnt = 0

print(group)