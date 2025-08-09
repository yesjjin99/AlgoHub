n, m = map(int, input().split())  # 사람의 수, 파티의 수
truth = set(map(int, input().split()[1:]))  # 이야기의 진실을 아는 사람의 번호
parties = [set(map(int, input().split()[1:])) for _ in range(m)]  # 각 파티마다 오는 사람의 번호

for _ in range(m):  # 새로운 사람이 진실을 알게 될 경우, 그 사람이 속한 파티가 있는지 모두 확인해야 하기 때문에 -> 파티의 수만큼 반복
    for party in parties:
        if party & truth:  # 파티에 진실을 아는 사람이 한 명이라도 있는 경우
            truth = truth.union(party)  # 그 파티의 모든 사람이 진실을 알게 됨

cnt = 0
for party in parties:
    if party & truth:
        continue
    cnt += 1

print(cnt)