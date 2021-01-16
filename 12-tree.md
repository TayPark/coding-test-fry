# 트리

- 계층적인 구조를 표현하는 자료구조
  - root: 최상위 노드
  - leaf: 최하위 노드
  - size: 트리에 포함된 모든 노드의 수
  - depth: 루트 노드부터의 거리
  - height: 깊이 중 최대값
  - degree: 각 노드의 간선 수
    - **트리의 크기가 N일 때, 전체 간선 수는 N-1**이다.

## 이진 탐색 트리

- 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조
  - 왼쪽 자식노드 < 부모 노드 < 오른쪽 자식 노드
- 원소를 찾는 과정
  1. 루트를 방문
  2. 루트보다 작다면 왼쪽, 크다면 오른쪽으로 이동
  3. 찾을 때까지 2 반복

## 트리 순회

- 트리 자료구조에 포함된 노드를 한 번씩 방문하는 방법
  - 전위 순회(pre-order): 루트를 먼저 방문
  - 중위 순회(in-order): 왼쪽 자식을 방문한 뒤에 루트를 방문
  - 후위 순회(post-order): 오른쪽 자식을 방문한 뒤에 루트를 방문

```py
# 7
# A B C
# B D E
# C F G
# D None None
# E None None
# F None None
# G None None
class Node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right

def pre_order(node):
  print(node.data, end=' ')
  if node.left != None:
    pre_order(tree[node.left])
  if node.right != None:
    pre_order(tree[node.right])

def in_order(node):
  if node.left != None:
    in_order(tree[node.left])sudo apt-get update && sudo apt-get install wget ca-certificates
  print(node.data, end=' ')
  if node.right != None:
    in_order(tree[node.right])

def post_order(node):
  if node.left != None:
    post_order(tree[node.left])
  if node.right != None:
    post_order(tree[node.right])
  print(node.data, end=' ')

n = int(input())
tree = {}

for i in range(n):
  data, left, right = input().split()
  if left == "None":
    left = None
  if right == "None":
    right == None
  tree[data] = Node(data, left, right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
```
