# 기타 그래프들

## 서로소 집합
: **공통 원소가 없는 두 집합**을 말한다.

- 서로소 **부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조**이다.
  - 그래프에서 **서로 다른 노드가 연결되어있는지 유무를 판단**한다.
- 서로소 집합 자료구조는 두 종류의 연산을 지원한다.
  - Union
  - Find
- 서로소 집합 자료구조는 **합치기 찾기(Union-Find) 자료구조**라고 불리기도 한다.

### Union-Find

1. 합집합 연산을 확인하여 서로 연결한 두 노드 A, B를 확인
  1. A와 B의 루트노드 A', B'를 각각 찾는다. (A < B) 루트노드를 찾는 과정은 재귀적으로 반복된다.
  2. A'를 B'의 부모 노드로 설정
2. 모든 합집합 연산을 처리할 때까지 1번의 과정을 반복

```py
def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블을 자기자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i

# Union 연산 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v+1):
  print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end=' ')
for i in range(1, v + 1):
  print(parent[i], end=' ')
```

### 문제점

- 합집합 연산이 편향적으로 이루어질 경우(5-4-3-2-1...) 찾기 함수가 비효율적으로 동작할 수 있다.
- 최악의 경우 모든 노드를 확인해야 하므로 O(V)이다.
  - Union(4, 5), Union(3, 4), Union(2, 3), Union(1, 2)

## Union-Find 최적화: 경로 압축

- Find 함수를 최적화하기 위해 경로 압축을 사용할 수 있다.
  - Find 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 갱신한다.
- 각 노드에 대해 Find 함수를 호출한 이후에 해동 노드의 루트 노드가 바로 부모 노드가 된다.
- 모든 Union 함수를 처리한 후에 각 원소에 대해 Find 함수를 수행하면 모두 부모가 1이된다.
  - 시간 복잡도가 개선된다

```py
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])  # 부모 테이블 값 갱신
  return parent[x] 
```

## 사이클 판별

- 서로소 집합은 **무방향 그래프(DAG) 내에서 사이클을 판별**할 때 사용할 수 있다
  - DFS를 사용해도 된다.
- 사이클 판별 알고리즘
  1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인한다.
    1. 루트 노드가 서로 다르다면 두 노드에 대해 Union 연산을 수행한다.
    2. 루트 노드가 서로 같다면 사이클이 발생한 것이다.
  2. 그래프에 포함되어있는 모든 간선에 대해 1번을 반복한다.

```py
# 경로 압축, Union-Find 코드는 동일
for i in range(e):
  a, b = map(int, input().split())
  if find_parent(parent, a) == find_parent(parent, b):  # find를 호출했을 때 부모가 같다면
    cycle = True
    break
  else: # 같지 않으면 union 호출
    union_parent(parent, a, b)

if cycle:
  # 사이클 발생
else:
  # 사이클 미발생
```

## 최소 신장 트리

- 신장 트리: 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
- 최소 신장트리: 그래프 상에서 간선을 효율적으로 사용하도록 한다.
  - 전체 간선의 갯수는 전체 노드의 수 - 1이다.(트리의 특성)

## 크루스칼 알고리즘

- 그리디 알고리즘으로 분류
1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 하나씩 확인하여 현재의 간선이 사이클을 발생시키는지 확인
  - 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
  - 사이클 발생 여부는 만들고 있는 트리 내에 간선을 가지는 2개의 노드가 모두 포함될 때 발생
3. 모든 간선에 대해 반복

- 간선의 개수가 E일때, O(ElogE)의 시간 복잡도를 가진다.
- 가장 많은 시간을 요구하는 곳은 간선을 정렬하는 부분

```py
def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 수와 간선의 개수 입력
v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v + 1)

# 부모 테이블을 자기자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i

edges = []
result = 0

# 부모 테이블을 
for _ in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b)) # 첫 원소 기준으로 정렬됨을 인지

edges.sort()

for edge in edges:
  cost, a, b = edge # 매 간선마다
  if find_parent(parent, a) != find_parent(parent, b):  # 사이클이 발생하지 않았을 경우
    union_parent(parent, a, b)  # 최소신장트리에 추가
    result += cost  # 전체 비용에 추가
```

## 위상 정렬

- 사이클이 없는 방향 그래프(`DAG`)의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
- 진입차수(Indegree): 특정 노드로 들어오는 간선의 개수
- 진출차수(Outdegree): 특정 노드에서 나가는 간선의 개수

1. 진입차수가 0인 모든 노드를 큐에 넣는다
2. 큐가 빌 때까지 반복
  1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
  2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다

- 결과적으로 **각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과**와 같다.
- 위상 정렬에는 여러가지 답이 존재할 수 있다. 
  - 한 단 계에서 큐에 들어가는 노드의 수가 2개 이상이면 여러가지 답이 존재
- **모든 원소를 방문하기 전에 큐가 빈다고 사이클이 존재한다고 판단**
- 스택을 활용한 DFS를 이용하여 위상 정렬을 수행할 수도 있다.
- 위상 정렬을 위해 차례대로 모든 노드를 확인하려면 각 노드에서 나가는 간선을 차례대로 제거해야한다.
  - 그러므로 시간 복잡도는 O(V+E) 이다. (V: 정점, E: 간선)

```py
from collections import deque

v, e = map(int, input().split())

# 진입차수와 그래프 생성
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

# 진입차수와 그래프 초기화
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

order = []

def topology_sort():
  q = deque()
  for i in range(1, v + 1): # 큐 초기화
    if indegree[i] == 0:  # 1. 큐에 진입차수가 0인 모든 노드 추가
      q.append(i)
  while q:  # 2. 큐가 빌 때까지
    now = q.popleft() 
    order.append(now) # 큐에서 나온 노드들은 정렬 가능
    for i in graph[now]:  # 해당 노드의 간선을 그래프에서 제거(진입차수를 1씩 뺀다)
      indegree[i] -= 1
      if indegree[i] == 0:  # 진입차수가 0이면
        q.append(i) # 큐에 추가

topology_sort()

for i in order: # 순서에 맞춰서 출력
  print(i, end=' ')
```