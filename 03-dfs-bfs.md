# DFS, BFS

- 많은 데이터 중 원하는 데이터를 찾는 과정

## 스택

- 리스트의 `.append()`와 `.pop()`을 사용하면 된다.
- 스택 최상단 원소부터 출력하는 방법
  - `print(stack[::-1])`

## 큐

- 덱(deque)을 사용 
  - 시간 복잡도가 높아 비효율적일 수 있다.

```py
from collections import deque

# 만약 deque를 사용할 수 없을 경우
# queue = list()
queue = deque()


queue.append(3)
# queue.pop(0)
queue.popleft() 
```

## 재귀함수

- DFS를 구현할 때 사용

## 팩토리얼 구현 예제

```py
def get_factorial(x):
  if x <= 1:
    return 1
  return x * get_factorial(x-1)
```

## 최대공약수 계산(유클리드 호제법)

- 두 자연수 A, B(A > B)에 대해 A를 B로 나눈 나머지를 R이라고 하자.
- 이 때 A와 B의 최대공약수는 B와 R의 최대 공약수와 같다.

```py
def gcd(x, y):
  r = x % y
  if r == 0:
    return y
  else:
    return gcd(y, r)


x, y = map(int, input().split())

print(gcd(x, y))
```

## DFS, 깊이 우선 탐색

- 스택이나 재귀함수를 이용
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
  3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복

- 파이썬에서 인접 노드를 중첩 리스트로 만들어서 관리할 수 있다.

```py
graph = [
  [], # 0번 노드가 없을 때. 있다면 채운다.
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * len(graph) # 노드가 8개이고 0번 노드를 사용하지 않으므로 9라고 적는다.

def dfs(graph, node, visited):
  # 현재 노드 방문처리
  visited[node] = True
  print(node, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[node]: # 현재 노드에 인접한 노드들에 대해
    if not visited[i]:  # 방문하지 않았을 경우
      dfs(graph, i, visited)  # dfs 수행

dfs(graph, 1, visited)
```

## BFS, 너비 우선 탐색

- 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
- 큐 자료구조 사용
  1. 탐색 시작을 큐에 넣고 방문 처리
  2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
  3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복

```py
from collections import deque

graph = [
  [], # 0번 노드가 없을 때. 있다면 채운다.
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * len(graph) # 노드가 N개일 때 숫자를 늘리면된다. 노드가 8개이고 0번 노드를 사용하지 않으므로 9라고 적는다.

def bfs(graph, node, visited):
  # 최초
  visited[node] = True
  queue = deque([node])

  while queue:  # queue가 비어있지 않으면
    v = queue.popleft() # dequeue 한다.
    print(v, end=' ')
    for i in graph[v]:  # 인접한 노드 중에
      if not visited[i]:  # 방문하지 않은 노드는
        queue.append(i)   # 큐에 추가
        visited[i] = True # 방문했다고 표시
  
bfs(graph, 1, visited)
```

## 음료수 얼려먹기

> N x M의 얼음 틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 있는 부분을 1이라고 한다. 구멍이 뚫려있는 부분이 상, 하, 좌, 우가 붙어있는 경우 연결되어있는 것으로 간주한다. 이 때, 얼음 틀의 모양이 주어지면 생성되면 총 아이스크림의 갯수를 구하라.

- 첫 번째 줄에 얼음 틀의 **세로길이 N**과 **가로길이 M**이 주어진다. 
- 두 번째 줄부터 N+1 번째 줄까지의 얼음 틀 형태가 주어진다.
- `DFS`로 풀이한다. 얼음을 만나면 1로 처리하여 재귀호출을 했을 때 읽지 못하도록 한다.

```py
def dfs(x, y):    # 얼음이면 True, 얼음틀이면 False 반환
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False  # 범위를 벗어나면 False
  if graph[x][y] == 0:  # 얼음이라면
    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True 
  return False  # 얼음이 아니면 False

n, m = map(int, input().split())

graph = list()
for i in range(n):  # 얼음틀 모양을 입력받음
  graph.append(list(map(int, input())))

result = 0

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True: # 얼음이면
      result += 1  # +1

print(result)
```

## 미로 탈출

> N x M 직사각형 미로에 갇혔다. 미로에는 여러 괴물이 있어 이를 피해 탈출해야한다. 나의 위치는 (1, 1)이며 미로의 출구는 (N, M)이고, 한 번에 한 칸만 이동할 수 있다. 괴물이 있는 부분은 0, 없는 부분은 1이다. 이 때, 탈출하기 위한 최소 칸의 수를 구하라.

- 첫 번째 줄에 얼음 틀의 **세로길이 N**과 **가로길이 M**이 주어진다. 
- 다음 N개의 줄에는 각각 M의 정수로 미로의 정보가 주어진다.
- 시작과 마지막 칸은 항상 1이다.

```py
from collections import deque

def bfs(x, y):
  # 큐 초기화
	queue = deque()
	queue.append((x, y))

	while queue:	# 큐가 비어있지 않으면
		a, b = queue.popleft()	# 하나 빼서
		for i in range(4):	# 상하좌우 모두 계산
			nx = a + dx[i]
			ny = b + dy[i]
			if nx < 0 or nx >= n or ny < 0 or ny >= m:	# 경계 밖이면 (n과 m이 밖이므로)
				continue
			if graph[nx][ny] == 0:	# 벽이면
				continue
			if graph[nx][ny] == 1:	# 갈 수 있는 길이면
				graph[nx][ny] = graph[a][b] + 1
				queue.append((nx, ny))

	return graph[n-1][m-1]

n, m = map(int, input().split())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []

for i in range(n):
	graph.append(list(map(int, input())))

print(bfs(0, 0))
```
