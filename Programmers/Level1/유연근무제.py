def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        h = (schedules[i] // 100) * 100
        m = schedules[i] % 100 + 10

        if m >= 60:
            schedules[i] = h + (m // 60) * 100 + (m % 60)
        else:
            schedules[i] += 10

    for i in range(len(timelogs)):
        now = startday
        count = 0

        for j in range(len(timelogs[i])):
            if 1 <= now <= 5 and timelogs[i][j] <= schedules[i]:  # 토요일, 일요일의 출근 시각은 제외
                count += 1

            now = (now + 1) % 7

        if count == 5:
            answer += 1

    return answer