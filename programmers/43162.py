# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

def DFS(computers, visited, v):
    if visited[v] == 0:
        visited[v] = 1
    for e in range(len(computers)):
        if computers[v][e] == 1 and visited[e] == 0:
            DFS(computers, visited, e)


def solution(n, computers):
    visited = [0] * n
    answer = 0
    while 0 in visited:  # 모두 방문할 때까지
        for i in range(n):  # 전체 노드(컴퓨터)에 대해 (처음 실행 이후에 묶이지 않은 곳만 남음)
            if visited[i] == 0:  # 방문하지 않았다면
                DFS(computers, visited, i)  # DFS 실행, 네트워크로 묶음
                answer += 1

    return answer
