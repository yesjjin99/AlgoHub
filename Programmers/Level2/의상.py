from collections import defaultdict

def solution(clothes):
    dic = defaultdict(int)
    for name, type in clothes:
        dic[type] += 1

    if len(dic) == 1:
        return list(dic.values())[0]

    answer = 1
    for d in dic.values():
        answer *= d + 1  # 선택을 안 하는 경우까지 포함하여 (각 종류의 개수 + 1)을 모두 곱한다!
    return answer  # 아무것도 선택 안했을 경우 제외(-1)


from collections import Counter
from functools import reduce

def solution(clothes):
    c = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), c.values(), 1) - 1
    return answer
