# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

from typing import List
    

def solution(record: List[str]):
    answer = []

    uid_nick_db = {}

    actions = []
    for event in record:
        info = event.split()
        action, uid = info[0], info[1]
        if action in ("Enter", "Change"):
            uid_nick_db[uid] = info[2]
        actions.append((action, uid))

    for action_info in actions:
        act, uid = action_info[0], action_info[1]
        if act == 'Enter':
            answer.append(f'{uid_nick_db[uid]}님이 들어왔습니다.')
        elif act == 'Leave':
            answer.append(f'{uid_nick_db[uid]}님이 나갔습니다.')    
    
    return answer