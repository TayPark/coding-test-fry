# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

def solution(board, moves):
    answer = 0
    bucket = []
    
    for i in moves:
        pos = i - 1
        for floor in board:
            target = floor[pos]
            if target != 0:
                floor[pos] = 0
                if len(bucket) > 0 and bucket[-1] == target:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(target)    
                break

    return answer