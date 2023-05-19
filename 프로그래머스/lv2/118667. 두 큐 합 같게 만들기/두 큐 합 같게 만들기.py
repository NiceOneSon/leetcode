from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    answer = 0
    limit = len(q1) + len(q2)
    limit *= 3
    while s1 != s2 and limit:
        limit -= 1
        if s1 > s2:
            num = q1.popleft()
            q2.append(num)
            s1 -= num
            s2 += num
        else:
            num = q2.popleft()
            q1.append(num)
            s2 -= num
            s1 += num
        answer += 1
            
    if s1 != s2:
        return -1
    return answer