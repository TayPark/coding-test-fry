# https://programmers.co.kr/learn/courses/30/lessons/76501?language=python3

def solution(absolutes, signs):
    answer = []
    for idx, value in enumerate(absolutes):
        if signs[idx]:
            answer.append(absolutes[idx])
        else:
            answer.append(- absolutes[idx])
    return sum(answer)

"""
다른 풀이
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
"""