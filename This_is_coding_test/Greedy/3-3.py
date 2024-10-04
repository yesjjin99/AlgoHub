n, m = map(int, input().split())
cards = []

for _ in range(n):
    cards.append(min(map(int, input().split())))

print(max(cards))