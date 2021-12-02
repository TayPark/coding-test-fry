# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

def solution(new_id):
    # 1
    new_id = new_id.lower()
    
    # 2
    tmp = ''
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            tmp += i
    
    new_id = tmp
    
    # 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
        
    # 4
    if new_id[0] == '.':
        new_id = new_id[1:] if len(new_id) > 1 else '.'
    if new_id[-1] == '.': new_id = new_id[:-1]
    
    # 5
    if new_id == '':
        return 'aaa'
    
    # 6
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # 7
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id