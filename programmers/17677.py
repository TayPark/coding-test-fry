# https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3

from collections import Counter

def solution(str1, str2):
    # 대소문자 차이가 없으므로 모두 소문자 처리
    str1, str2 = str1.lower(), str2.lower()
    one_list, two_list = [], []
    
    # 두 글자씩, 영문자만 유효하므로 검증 처리
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            one_list.append(str1[i] + str1[i + 1])
    
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            two_list.append(str2[i] + str2[i + 1])
    
    # union, intersect 사용을 위해 Counter 사용
    cnt_one = Counter(one_list)
    cnt_two = Counter(two_list)
    
    inter = list((cnt_one & cnt_two).elements())
    union = list((cnt_one | cnt_two).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    
    return int(len(inter) / len(union) * 65536)