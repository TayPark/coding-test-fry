# https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3

def solution(bridge_length, weight, truck_weights):
    time = 0
    road = [0] * bridge_length
    
    while road:
        time += 1
        road.pop(0) # 도로 끝에 트럭이 있다면 통과
        if truck_weights:   # 남은 트럭이 있다면
            if sum(road) + truck_weights[0] <= weight:  # 현재 다리가 버틸 수 있는 무게라면
                road.append(truck_weights.pop(0))   # 뒤에 추가
            else:
                road.append(0)  # 그렇지 않으면 도로 유지
    
    return time