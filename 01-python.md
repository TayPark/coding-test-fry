# 파이썬 기본

## 정수

```py
c = '10'
int(c)
print(c)  # 10
```

- `/`: 나눠진 결과를 실수형으로 반환
- `%`: 나머지 연산
- `//`: 몫 연산자
- `**`: 거듭제곱 연산

## 실수

- 소수부가 0이거나, 정수부가 0인 소수는 0을 생략하고 작성할 수 있다.
- 지수는 1e9 (10^9) 처럼 표현할 수 있다. e는 10을 몇 번 곱할것인지 나타낸다.
  - 최단경로 알고리즘에서 최대값이 10억 미만이라면 무한의 값으로 1e9를 이용할 수 있다.
- IEEE 754 표준에서 실수를 저장하기 위해 4바이트 혹은 8바이트를 사용하기 때문에, 컴퓨터 시스템은 실수 정보를 표현하는데 정확도의 한계가 있다.
  - 그러므로 반올림, round(정수형, 표현한계숫자)를 사용하자.
  - round(123.456, 2) == 123.46

## 리스트 []

- 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
- 배열과 유사
- 리스트 슬라이싱
  - : 을 넣어 시작과 끝 인덱스+1 설정 
- 리스트 초기화
  - list()
  - []
  - [i for i in range(10)]
    - 2차원 리스트를 초기화할 때 효과적
    - array = [[0] * m for _ in range(n)]: 0원소를 가진 M X N 크기의 2차원 리스트 초기화
    - `_`: 파이썬에서 반복을 수행하되 반복을 위한 변수의 값을 무시
```py
arr = [i for i in range(5)]   # a = [0, 1, 2, 3, 4]
arr.sort(reverse = True)      # 내림차순으로 정렬
arr.append(1)                 # a = [0, 1, 2, 3, 4, 1]
arr.reverse()                 # a = [1, 4, 3, 2, 1, 0]
arr.remove(2)                 # a = [1, 4, 3, 1, 0]
arr.insert(0, 99)             # a = [99, 1, 4, 3, 1, 0]
print(arr.count(1))           # 2

remove_set = {3, 5}         # 특정 원소를 모두 제거하기 위해 Set 자료형 만듦
result = [i for i in arr if i not in remove_set]
```

## 문자열

- 문자열 변수에 양의 정수를 곱하면 문자열이 그 값만큼 여러번 더해진다.
- 문자열에 대해서 인덱싱과 슬라이싱이 가능하나 특정 인덱스의 값을 바꿀 수는 없다(새로 만들어야 한다.)
- 정수형에 대해서 `str(INTEGER)` 로 형변환한다.

## 튜플 ()

- 선언되면 변경이 불가능
- 소괄호 사용
- 공간 효율적
- 서로 다른 성질의 데이터를 묶어서 관리할 때
  - 최단 경로 알고리즘에서 (비용, 노드번호)의 형태로 사용
- 데이터 나열을 해시 키값으로 사용
  - 변경이 불가능하므로 키값으로 사용 가능

## 딕셔너리

- K-V
- 내부에서 해시테이블을 사용하므로 조회 및 수정에 O(1)시간에 처리가 가능
- 해당 데이터들은 **dict_keys, dict_values 형태로 나오기때문에 list로 형변환이 필요**
- 키 데이터만 뽑을 때: list(dict.keys())
- 값 데이터만 뽑을 때: list(dict.values())

## 집합

- 중복 불허
- set() 함수로 초기화
  - set(LIST[]) 이면 중복을 제거하고 새로운 집합 반환
  - data = { 1, 1, 3, 2, 3 } 이면 중복을 제거하고 새로운 집합 반환
- 데이터 조회 및 수정에 있어 O(1) 시간 내에 처리
- `|` : 합집합
- `&` : 교집합
- `-` : 차집합

```py
a = set([1, 1, 3, 2, 5, 3, 1])    # {1, 2, 3, 5}
a.add(5)
a.update([11, 23])
a.remove(1)
```

## 표준 입력

- input(): 한 줄 문자열 입력
- map(): 리스트 모든 원소에 특정 함수를 적용

```py
# 11 22 33 44 55 로 입력을 받는다고 가정
score_data = list(map(int, input().split())) # [11, 22, 33, 44, 55]

# 3개의 정수를 한번에 a, b, c에 저장
a, b, c = map(int, input().split()) # 1, 2, 3
```

- 입력이 굉장히 많은 경우, 입력을 최대한 빠르게 받아야한다.
  - **이진탐색, 정렬, 그래프 문제에서 사용**
- 파이썬의 경우 sys 라이브러리의 sys.stdin.readline() 메서드 이용
- Enter가 줄바꿈 기호로 입력되므로 rstrip() 메서드 함께 이용
  - import sys
  - `data = sys.stdin.readline().rstrip()`

## 표준 출력

- print()를 사용한다.
- print()는 기본적으로 줄바꿈을 하므로, `print(1, end=" ")` 처럼 사용하면 공백으로 바꿀 수 있다.
- f-string: Python 3.6~. JS 템플릿.
  - `print(f"정답은 {score}입니다.")`

## 조건문

- `if ~ elif ~ else`
- 논리 연산자
  - X `and` Y
  - X `or` Y
  - `not` X
- `in` 연산자
  - 리스트, 튜플, 문자열, 딕셔너리 모두 사용가능
  - `x in DATA, x not in DATA` 로 사용
- `pass`
  - 해당 구문을 실행하지 않음

## 반복문

- range()
  - 연속적인 값을 순회할 경우
  - range(시작, 끝값+1)
  - 인자를 하나만 넣으면 시작값이 0이 된다.
- countinue
  - 남은 코드를 건너뛰고 다음 반복을 진행

## 함수

- global
  - 해당 함수는 지역 변수를 만들지 않고 함수 바깥에 선언된 변수를 참조

```py
a = 0

def func():
  global a
  a += 1
```

- 함수는 여러 반환값을 가질 수 있다.
- 람다 표현식을 사용하면 함수를 간단하게 사용할 수 있다

```py
print((lambda a, b: a + b)(3, 7))

# 내장 함수에서 사용되는 람다함수
array = [('kim', 62), ('lee', 11), ('Ahn', 24)]
def my_key(x):
  return x[1]

print(sorted(array, key=my_key))

# 람다 sorted(interable, key)
print(sorted(array, key=lambda x: x[1]))

# 람다를 이용한 리스트 덧셈
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda a, b: a + b, list1, list2) # [7, 9, 11, 13, 15]
```

## 실전 라이브러리

- itertools: 반복 데이터를 처리
  - 순열, 조합
- heapq: 힙 자료구조 제공. 우선순위 큐
- bisect: 이진탐색
- collections: 덱, 카운터 등의 자료구조
- math: 수학적 기능(팩토리얼, 제곱근, GCD, pi 등)

```py
sum([1, 2, 3, 4, 5])  # 리스트 합
min()   # 최소값
max()   # 최대값
eval("(3+5)*7") # 수식 계산
sorted() # 리스트 정렬. 역순은 reverse=True

```

- 순열과 조합
  - 순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열
  - 조합: 서로 다른 n개에서 서로 다른 r개를 선택

```py
from itertools import permutations, combinations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))    # data에서 3개를 뽑는 순열
result2 = list(combinations(data, 2))   # data에서 2개를 뽑는 조합
```

- 중복 순열과 중복 조합

```py
from itertools import product, combinations_with_replacement

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))  # 중복(A, A)을 포함한 2개를 뽑는 모든 순열

result2 = list(combinations_with_replacement(data, 2)) # 중복을 포함한 2개를 뽑는 모든 조합
```

- 카운터
  - 원소의 등장 횟수 카운트

```py
from collections import Counter

counter = Counter(['red', 'green', 'red', 'orange', 'red', 'green', 'orange', 'red'])
print(counter['green']) # 등장 횟수 출력
print(dict(counter))  # 딕셔너리 자료형으로 반환
```

- 최대 공약수(GCD)

```py
import math

print(math.gcd(21, 14))

def lcm(a, b):  # 최소 공배수
  return a * b // math.gcd(a, b)  

print(lcm(21, 14))
```