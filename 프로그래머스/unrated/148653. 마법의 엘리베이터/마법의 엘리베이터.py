from collections import deque

def go_up(number):
    c = 1
    while number % 10 ** c < 1:
        c += 1
    alpha = 10 ** (c) - number % 10 ** c
    return alpha // 10 ** (c - 1) , alpha 

def go_down(number):    
    c = 1
    while number % (10 ** c) < 1:
        c += 1
    resid = number % (10 ** c)
    alpha = resid // (10 ** (c-1))
    return alpha, resid
    

def solution(storey):
    answer = float('inf')
    q = deque([(storey, 0)])
    
    while q:
        number, cnt = q.popleft()
        if number == 0:
            answer = min(answer, cnt)
            continue
        elif cnt > answer:
            continue
        elif number < 0:
            continue
        addcnt, higher = go_up(number)
        q.append((number + higher, cnt + addcnt))
        addcnt, lower = go_down(number)
        q.append((number - lower, cnt + addcnt))
    return answer