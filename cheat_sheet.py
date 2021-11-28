###
# 캐스팅(변환) -> int(), str()
###
string = '1234'
print(int(string)) # 숫자 1234

integer = 1234
print(str(integer)) # 문자열 1234

###
# 최대 최소 -> min(), max()
###
num_list = [1, 2, 3, 4]
mini = min(num_list)  # 1
maxi = max(num_list)  # 4
str_list = ['b', 'c', 'w', 'z']
mini = min(str_list)  # b
maxi = max(str_list)  # z

###
# 숫자 0부터 N까지 리스트 만들기
###
num_list = list(range(50))
print(num_list) # [0, 1, 2, 3, 4, ...]

###
# 알파벳인지 확인
###
char = 'a'
if char.isalpha():
  print(True) # True

###
# 숫자인지 확인
###
char = '1'
if char.isdigit():
    print(True) # True

###
# 리스트를 문자로 합치기
###
str_arr = ['a', 'b', 'c', 'd', 'e']
print(''.join(str_arr)) # abcde

###
# 문자열을 리스트로
###
str = 'abcde'
str_arr = list(str)
print(str_arr)  # ['a', 'b', 'c', 'd', 'e']

###
# 2차원 배열
###
# 만들지 마라. 뇌속으로 생각해라.

###
# 표준 입력 처리 
###
# 11 22 33 44 55 를 받는다고 가정
score_data = list(map(int, input().split())) # [11, 22, 33, 44, 55]
print(score_data)
# 3개의 정수를 한번에 a, b, c에 저장
a, b, c = map(int, input().split())
print(a, b, c)
# 101101 -> [1, 0, 1, 1, 0, 1]
each_num = list(map(int, input()))
print(each_num)

###
# 최소공배수, 최대공약수(LCM, GCD)
###

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

###
# 치환 -> replace()
###

a = "1234"
a.replace("2", "5") # "1534"

###
# 리스트 인덱스 관련
###

a = [1, 2, 3, 4]
print(a.index(3)) # 2

###
# 리스트 중복체크 -> List len과 Set의 len을 비교
###

a = [1, 2, 3, 3]
list_has_dup = len(a) == len(set(a))

print(list_has_dup) # False
