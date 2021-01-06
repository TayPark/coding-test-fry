# 최단경로 알고리즘

- 한 지점에서 다른 한 지점까지의 최단 경로
- 한 지점에서 다른 모든 지점까지의 최단 경로
- 모든 지점에서 다른 지점까지의 최단 경로

## 다익스트라

- 특정 노드에서 출발하여 다른 모든 노드로 가는 최단경로 계산
- **음의 간선이 없을 때 정상적으로 동작**
- 그리디 알고리즘으로 분류
  - 매 상황에서 가장 적은 비용의 노드를 선택
- 단계를 거치며 한 번 처리된 노드의 최단거리는 고정되어 바뀌지 않음
- 최단경로를 구하려면 추가적인 알고리즘 필요

1. 출발 노드 설정
2. 최단거리 테이블 초기화
3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 **최단거리 테이블 갱신**
5. 반복

```py
n, m = map(int, input().split())  # 노드 수, 간선 수
start = int(input())  # 시작 노드 번호
graph = [[] for i in range(n + 1)]  # 그래프 초기화
visited = [False] * (n + 1) # 방문 초기화
distance = [-1] * (n + 1) # 거리 초기화

for _ in range(m): # 인덱스와 관련없이 입력받는 값을 abc에 입력받음
  a, b, c = map(int, input().split())
  graph[a].append((b, c)) # 그래프 입력

def get_smallest_node():  # 그래프 노드
  min_value = -1
  index = 0
  for i in range(1, n + 1): # 그래프가 1부터 n까지이므로
    if distance[i] != min_value and not visited[i]: # 거리를 아는 노드 중 방문하지 않은 노드
      min_value = distance[i] # 
      index = i
    return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  for _ in range(n - 1):
    now = get_smallest_node()
    visited[now] = True
    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == -1:
    print("INF")
  else:
    print(distance[i])
```

- 총 O(V)번에 걸쳐 최단거리가 가장 짧은 노드를 매번 선형 탐색해야 함
- 따라서 시간 복잡도는 O(V^2)
- 전체 노드 수가 `5,000개 이하`라면 문제를 해결할 수 있음

## 우선순위 큐(Priority Queue)

- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
- Python, Java, C++에서 표준 라이브러리로 지원

## Heap

- Priority Queue를 구현하기 위해 사용하는 자료구조 중 하나
- 트리로 구현, O(logN) 보장
- Min Heap과 Max Heap

| 우선순위 큐 구현 방식 | 삽입 시간 | 삭제 시간 |
| ------------------ | ------- | -------- |
| 리스트              | O(1)    | O(N)     |
| 힙                 | O(logN) | O(logN)  |

- 파이썬에서 heap 라이브러리를 사용
  - heappush, heappop
- Min Heap을 지원. 우선순위가 낮은 데이터부터 나오는 특성을 가짐

```py
# Min Heap
import heapq

def heapsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h, value)
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

# Max Heap
def heapsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h, -value) # 부호를 바꿔서 넣고
  for i in range(len(h)):
    result.append(-heapq.heappop(h))  # 꺼낼 때 부호를 바꿔서 빼면 된다
  return result
```

- 단계마다 방문하지 않은 노드 중 최단거리가 가장 짧은 노드를 선택하기 위해 Heap을 이용
- 기본 원리는 동일하나, 가장 가까운 노드를 저장하기 위해 Heap을 추가적으로 이용한다는 점이 다름
  - 최단거리가 가장 짧은 노드를 선택하므로 Min Heap을 사용

```py
# 입력
# n: 노드 수, m: 간선 수
# 이하의 k 줄의 a, b, c: a노드에서 c노드로 가는 간선의 비용 b

import heapq

n, m = map(int, input().split())

start = int(input())
graph = [[] for x in range(n+1)]
distance = [-1] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c)) # 튜플 형태로 삽입(데이터가 변하지 않으므로)

def dijkstra(start):
  q = []  # 비용에 따른 우선순위 큐 
  heapq.heappush(q, (0, start)) # 우선순위 큐에 시작 노드에 대한 정보(거리, 노드)를 삽입
  distance[start] = 0 # 거리 초기화
  while q:  # 큐가 빌 때까지 수행
    dist, now = heapq.heappop(q)  # 최단거리가 짧은 노드의 정보 꺼냄
    if distance[now] < dist:  # 이미 최단경로가 있다면 계산하지 않음(=이미 방문했음)
      continue
    for i in graph[now]:  # 현재 노드에서 갈 수 있는 경로들에 대해
      cost = dist + i[1]  # 해당 노드로 가는 경로 = 현재 노드 비용 + 가는 비용
      if cost < distance[i[0]]: # 더 최적이라면
        distance[i[0]] = cost # 바꾸고
        heapq.heappush(q, (cost, i[0])) # 해당 노드를 우선순위 큐에 삽입

dijkstra(start)

for k in range(1, n + 1):
  if distance[k] == -1:
    print("INFINITY")
  else:
    print(distance[k])
```

## 플루이드 워셜

- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
- 단계별로 거쳐가는 노드를 기준으로 알고리즘을 수행
  - 매 단계마다 방문하지 않은 노드 중 최단거리를 갖는 노드를 찾는 과정이 필요하지 않음
- 플루이드 워셜은 **2차원 테이블에 최단 거리 정보를 저장**
- 일종의 **다이나믹 프로그래밍**
- 각 단계마다 특정한 노드 k를 거쳐가는 경우를 확인
  - a에서 b로 가는 최단거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사
  - Dab = min(Dab, Dak + Dkb)
- 3중 루프가 들어가는 알고리즘
  - 구현하기는 쉽지만 500 이상의 문제에 대해서는 쓰지 말자.

```py
n, m = map(int, input().split())

graph = [[-1] * (n + 1) for _ in range(n + 1)]

# 모든 그래프에서 자기자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):  
  for b in range(1, n + 1): 
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c

# 플루이드 워셜 알고리즘 수행
for i in range(1, n + 1):
  for j in range(1, n + 1):
    for k in range(1, n + 1):
      graph[j][k] = min(graph[j][k], graph[j][n] + graph[n][k])

# 출력
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == -1:
      print("INF", end=' ')
    else:
      print(graph[a][b], end=' ')
  print()
```

## 전보 문제

- N개의 도시가 있다고 가정하자. 도시 X에서 Y로 메시지를 전달하려면 통로를 거쳐야한다. 통로마다 비용이 다르다.
- 어느 날 C 도시에서 위급상황이 발생했다. 최대한 많은 도시로 메시지를 보내고자 한다. 각 도시의 번호와 통로가 설치된 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받는 도시의 수와 도시들이 메시지를 모두 받는데 걸리는 시간을 출력하는 프로그램을 작성하라.
- 첫 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내는 C가 주어진다.
  - 1 <= N <= 30,000, 1<= M <= 200,000, 도시 1<= C <= N, 비용 1<= Z <= 1,000 
- 둘째 줄 부터 M + 1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다. 특정 도시 X에서 Y로 가는 통로가 있고 통로 비용이 Z라는 의미이다.

문제 해결
- 노드의 수가 많으므로 개선된 다익스트라 알고리즘을 사용한다.
- 보내는 도시의 수는 전체 도시에서 보낼 수 없는 도시의 수를 뺀다.
- 보내는데 총 걸리는 시간은 전체 시간 중에서 가장 큰 값을 출력한다.

```py
import heapq

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)
distance = [INF] * (n + 1)

for _ in range(m):  # 간선 정보 입력 (출발, 도착, 비용)
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)  # 큐에서 가장 cost가 적은 노드를 뽑아옴
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_instance = 0

for d in distance:
  if d != INF:
    count += 1
    max_instance = max(max_instance, d)

print(count - 1, max_instance)
```

## 방문 판매원의 하루

- 모든 도시들은 모두 비용이 1이며, 양방향으로 이동 가능한 도로로 연결되어있다.
- 방문 판매원은 현재 1번 도시에 있고 X번 도시에 방문해 물건을 판매하고자 한다
- 오늘 방문 판매원은 소개팅에 참여하려 한다. 방문판매원은 1번 도시에서 출발하여 K 도시를 방문한 뒤에 X 도시로 가는 것이 목표이다.
- 도시 사이를 이동하는 최소 시간을 계산하는 프로그램을 작성하라
- 입력
  - 첫째 줄에 전체 회사 수 N과 경로의 수 M. 1 <= N, M <= 100
  - 둘째 줄 부터 M + 1 까지 연결된 두 회사의 번호가 주어진다.
  - M + 2 줄에는 목표지점 X와 경유지 K가 주어진다.
- 출력
  - 최소 이동 시간을 출력한다. 만약 갈 수 없다면 -1을 출력한다.

```py
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에 대한 경로는 없으므로 0
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j:
      graph[i][j] = 0

# 도시마다 연결된 선 등록
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

# 경유지와 목적지 입력
x, k = map(int, input().split())

# 플루이드 워셜 알고리즘 적용
for k in range(1, n + 1): # 경유지 K에 대해
  for a in range(1, n + 1): # 출발지 A와
    for b in range(1, n + 1): # 도착지 B에 대해
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # 더 빠른 길이 있다면 등록

distance = graph[1][k] + graph[k][x]

if distance >= INF:
  print(-1)
else:
  print(distance)
```