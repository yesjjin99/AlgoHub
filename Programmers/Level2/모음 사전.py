from itertools import product

def solution(word):
    words = []

    for i in range(1, 6):
        for s in product(['A', 'E', 'I', 'O', 'U'], repeat = i):
            words.append("".join(s))

    words.sort()
    return words.index(word) + 1
