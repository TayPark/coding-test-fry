# https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3

def solution(tickets):
    routes = {}
    
    for depart, arrival in tickets:
        if depart in routes.keys():
            routes[depart].append(arrival)
        else:
            routes[depart] = [arrival]
            
    for route in routes:
        routes[route].sort(reverse=True)
        
    stack = ['ICN']
    path = []
    
    while stack:
        top = stack[-1]
        if top in routes and routes[top]:   # 출발-도착 목록에 있으면서 경로가 비어있지 않을 경우
            stack.append(routes[top].pop())
        else:
            path.append(stack.pop())
    
    return path[::-1]