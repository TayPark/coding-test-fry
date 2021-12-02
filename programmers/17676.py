# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3

# 21:00:00.966
def get_ms(time):
    h = int(time[:2]) * 3600
    m = int(time[3:5]) * 60
    s = int(time[6:8])
    ms = int(time[9:])
    
    return (h + m + s) * 1000 + ms

# 21:00:00.966, 0.351s
def get_start_time(time, duration):
    n_time = duration[:-1]
    duration_time_ms = int(float(n_time) * 1000)
    # 시작 시간이므로 +1
    return get_ms(time) - duration_time_ms + 1

def solution(lines):
    answer = 0
    start_time = []
    end_time = []
    
    for line in lines:
        _, timestamp, duration = line.split()
        start_time.append(get_start_time(timestamp, duration))
        end_time.append(get_ms(timestamp))
    
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)
        
    return answer