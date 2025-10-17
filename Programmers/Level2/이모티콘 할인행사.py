from itertools import product

def solution(users, emoticons):
    answer = []
    sales = list(product([0.4, 0.3, 0.2, 0.1], repeat=len(emoticons)))  # 모든 이모티콘 할인율 조합

    for s in sales:
        plus, total = 0, 0  # 현재 할인율 조합으로 계산한 플러스 서비스 가입자수, 이모티콘 판매액

        for p, t in users:
            result = 0  # 이모티콘 구매비용의 합
            for i, e in enumerate(emoticons):
                if s[i] * 100 >= p:  # 해당 이모티콘 할인율이 기준 비율이상이면
                    result += e * (1 - s[i])

            if result >= t:  # 이모티콘 구매 비용이 사용자의 기준 가격 이상이면
                plus += 1
            else:
                total += result

        answer.append([plus, total])

    answer.sort(reverse=True)

    return answer[0]