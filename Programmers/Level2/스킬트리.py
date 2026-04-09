def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        seq = [i for i in tree if i in skill]
        if seq == list(skill[:len(seq)]):
            answer += 1
    return answer