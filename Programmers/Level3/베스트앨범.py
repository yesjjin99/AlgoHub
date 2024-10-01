from collections import defaultdict

def solution(genres, plays):
    answer = []
    gen = defaultdict(int)
    pl = defaultdict(list)

    for i, (g, p) in enumerate(zip(genres, plays)):
        gen[g] += p
        pl[g].append((p, i))

    gen = sorted(gen.items(), key=lambda x: x[1], reverse=True)
    for g, _ in gen:
        songs = sorted(pl[g], key=lambda x: x[0], reverse=True)
        answer.append(songs[0][1])
        if len(songs) > 1:
            answer.append(songs[1][1])
    return answer
