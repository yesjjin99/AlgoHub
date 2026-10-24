def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        tmp = [i for i in tree if i in skill]
        if tmp == list(skill[:len(tmp)]):
            answer += 1

    return answer