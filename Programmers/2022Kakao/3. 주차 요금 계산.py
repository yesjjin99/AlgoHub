from math import ceil

def solution(fees, records):
    answer = []
    cars = dict()

    # fees : 기본 시간, 기본 요금, 단위 시간, 단위 요금
    # records : 시각, 차량번호, 내역(in, out)
    for record in records:
        time, num, flag = record.split(" ")
        time = int(time.split(':')[0]) * 60 + int(time.split(':')[1])

        if flag == "IN":
            if num not in cars:
                cars[num] = [0, time, True]  # 누적 주차 시간, 가장 최근의 입차 시간, 입차 여부
            else:
                cars[num][1] = time
                cars[num][2] = True
        else:
            cars[num][0] += time - cars[num][1]
            cars[num][2] = False  # 출차 완료

    max_time = 23 * 60 + 59
    for i in cars.keys():
        if cars[i][2]:  # 입차된 후에 출차된 내역이 없다면
            cars[i][0] += max_time - cars[i][1]
            cars[i][2] = False

    # 기본 요금 + ceil(max((total - 기본 시간), 0) / 단위 시간) * 단위 요금
    for i in cars.keys():
        # 누적 주차 시간이 기본 시간이하라면, 기본 요금 청구
        answer.append((i, fees[1] + ceil(max((cars[i][0] - fees[0]), 0) / fees[2]) * fees[3]))
    answer.sort()

    return [i for _, i in answer]