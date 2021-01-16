# Lowest Common Ancestor, 최소 공통 조상 문제

N (2 ~ 50,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지의 번호가 매겨져있고, 루트는 1번이다. 두 노드의 쌍 M(1 ~ 10,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

1. 모든 노드의 깊이를 계산(DFS)
2. 최소 공통 조상을 찾을 두 노드를 확인
  - 먼저 두 노드의 깊이가 동일하도록 거슬러 올라간다
  - 이후 부모가 같아질 때까지 반복적으로 부모 방향으로 1칸씩 거슬러 올라간다.
3. 모든 LCA(a, b)연산에 대해 2의 과정을 반복

```py
n = int(input())

parent = [0] * (n + 1)  # 부모 노드 정보
node_depth = [0] * (n + 1) # 각 노드의 깊이
checked = [0] * (n + 1) # 각 노드의 깊이가 계산되어있는지 여부
tree = [[] for _ in range(n + 1)] 

for _ in range(n - 1):
  a, b = map(int, input().split())
  tree[a].append[b]
  tree[b].append[a]

def dfs(x, depth):
  checked[x] = True
  node_depth[x] = depth
  for y in tree[x]:
    if checked[y]:  # 이미 깊이를 구했을 경우
      continue
    parent[y] = x
    dfs(y, depth + 1)

def lca(a, b):
  while node_depth[a] != node_depth[b]: # depth가 동일하도록
    if node_depth[a] > node_depth[b]:
      a = parent[a]
    else:
      b = parent[b]
  while a != b: # 부모가 같아지도록
    a = parent[a]
    b = parent[b]
  return a

dfs(1, 0) # 루트 번호, depth 0

m = int(input())

for i in range(m):
  a, b = map(int, input().split())
  print(lca(a, b))
```

- 매 쿼리바다 부모 방향으로 거슬로 올라가기 위해 최악의 경우 O(N)의 시간 복잡도 요구
  - 따라서 모든 쿼리를 처리할 때 시간 복잡도는 O(NM)

## 심화 문제

N(2 ~ 100,000)개의 정점으로 이루어진 트리가 있다. 트리의 정점은 1부터 N까지 번호가 있고, 루트는 1번이다. 두 노드의 쌍 M(1 ~ 100,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

- N과 노드의 쌍 M이 커졌다. 더 효율적인 알고리즘이 필요하다.
  - 만약 한 칸씩 올라가는게 아니라 2의 제곱만큼 올라간다면 더 빠르게 찾을 수 있을 것이다.
  - 메모리를 더 사용하여 각 노드에 대해 2^i번째 부모에 대한 정보를 기록

1. 두 노드의 깊이를 맞춘다.
2. 거슬러 올라갈 때 2의 제곱만큼 올라가도록 한다.
