from collections import deque

def solution(n, t, m, timetable):
    # timetable을 분으로 변환하여 정렬합니다.
    ntable = []
    for time in timetable:
        minute = int(time[:2]) * 60 + int(time[3:])
        ntable.append(minute)
    ntable.sort()

    # 첫 셔틀 시간은 9:00 (분으로 계산)
    shuttle_time = 9 * 60
    
    # 마지막으로 탈 수 있는 시간을 기록할 변수
    last_time = 0
    
    # 셔틀 운행 횟수(n번 만큼) 반복
    for _ in range(n):
        q = deque()
        
        # 셔틀에 최대 m명까지 태울 수 있는 반복문
        while len(q) < m and ntable and ntable[0] <= shuttle_time:
            q.append(ntable.pop(0))

        # 마지막 셔틀인 경우, 내가 탈 수 있는 가장 늦은 시간을 계산
        if len(q) < m:
            last_time = shuttle_time  # 자리가 남으면 셔틀 시간에 맞춰 탈 수 있음
        else:
            last_time = q[-1] - 1  # 자리가 꽉 차면 마지막 탄 사람보다 1분 먼저 도착해야 함

        # 다음 셔틀 시간을 계산
        shuttle_time += t

    # last_time을 다시 HH:MM 형식으로 변환
    ah = str(last_time // 60).zfill(2)
    am = str(last_time % 60).zfill(2)
    
    return ah + ':' + am
