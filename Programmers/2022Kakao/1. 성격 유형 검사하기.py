from collections import defaultdict

def solution(survey, choices):
    answer = ''
    scores = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    type = defaultdict(int)

    for i in range(len(choices)):
        a, b = survey[i]
        if choices[i] in (1, 2, 3):
            type[a] += scores[choices[i]]
        else:
            type[b] += scores[choices[i]]

    answer += 'R' if type['R'] >= type['T'] else 'T'
    answer += 'C' if type['C'] >= type['F'] else 'F'
    answer += 'J' if type['J'] >= type['M'] else 'M'
    answer += 'A' if type['A'] >= type['N'] else 'N'
    return answer
