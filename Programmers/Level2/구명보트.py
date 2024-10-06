# 제한사항 꼼꼼히 확인하기!!
from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))

    while people:
        right = people.pop()  # 가장 무거운 사람부터 보트에 태우기
        if not people:
            return answer + 1

        if right + people[0] <= limit:  # 만약 가장 무거운 사람의 보트에 가장 가벼운 사람이 탈 수 있다면 태우기
            people.popleft()
        answer += 1

    return answer
