# https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3

def solution(words, queries):
    answer = []
    
    for q in queries:
        cnt = 0
        if q[0].isalpha():
            for w in words:
                if len(w) == len(q):
                    if w.startswith(''.join(q.replace('?', ''))):
                        cnt += 1
        else:
            for w in words:
                if len(w) == len(q):
                    if w.endswith(''.join(q.replace('?', ''))):
                        cnt += 1
        answer.append(cnt)
    
    return answer