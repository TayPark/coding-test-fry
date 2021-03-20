# https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3

def solution(m, n, puddles):
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    graph[1][1] = 1
    
    # 오른쪽이나 아래로밖에 이동할 수 없음
    # 그 길을 갈 수 있는 최단거리의 수를 구해야 함
    for i in range(1, n + 1):   # 세로
        for j in range(1, m + 1):   # 가로
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                graph[i][j] = 0
            else:
                graph[i][j] = graph[i - 1][j] + graph[i][j - 1]
    
    return graph[n][m] % 1000000007