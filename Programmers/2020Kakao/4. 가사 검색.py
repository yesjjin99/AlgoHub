# 가사 검색
from bisect import bisect_left, bisect_right
from collections import defaultdict

def solution(words, queries):
    answer = []
    words.sort()
    reverse_words = sorted([w[::-1] for w in words])
    count, check = defaultdict(int), defaultdict(list)
    for w in words:
        count[len(w)] += 1

    for j, q in enumerate(queries):
        if len(check[q]) != 0:  # 검색 키워드가 중복된 경우 -> 효율성 테스트
            answer.append(answer[check[q][0]])
            check[q].append(j)
            continue
        if q.count('?') == len(q):  # "?????" 같은 경우 -> 효율성 테스트
            answer.append(count[len(q)])
            check[q].append(j)
            continue

        cnt = 0
        if q[0] == '?':  # 접두사로 ? 가 붙을 때
            q = q[::-1]
            x = q.index('?')
            left, right = bisect_left(reverse_words, q[:x]), bisect_right(reverse_words, q[:x] + 'z' * (len(q) - x))
            for i in range(left, right):
                if len(reverse_words[i]) == len(q):
                    cnt += 1

        elif q[-1] == '?':  # 접미사로 ? 가 붙을 때
            x = q.index('?')
            left, right = bisect_left(words, q[:x]), bisect_right(words, q[:x] + 'z' * (len(q) - x))
            for i in range(left, right):
                if len(words[i]) == len(q):
                    cnt += 1

        answer.append(cnt)
        check[q].append(j)

    return answer

# ---

from bisect import bisect_left, bisect_right

def count(words, left_value, right_value):
    right_index = bisect_right(words, right_value)
    left_index = bisect_left(words, left_value)

    return right_index - left_index

def solution(words, queries):
    answer = []
    data = [[] for _ in range(10001)]  # 모든 단어를 길이마다 나누어서 저장 -> 효율성
    reverse = [[] for _ in range(10001)]

    for word in words:
        data[len(word)].append(word)
        reverse[len(word)].append(word[::-1])

    for i in range(10001):
        data[i].sort()
        reverse[i].sort()

    for query in queries:
        if query.startswith('?'):
            reversed_query = query[::-1]
            left_value = reversed_query.replace('?', 'a')
            right_value = reversed_query.replace('?', 'z')

            result = count(reverse[len(query)], left_value, right_value)

        else:
            left_value = query.replace('?', 'a')
            right_value = query.replace('?', 'z')

            result = count(data[len(query)], left_value, right_value)

        answer.append(result)
    return answer
