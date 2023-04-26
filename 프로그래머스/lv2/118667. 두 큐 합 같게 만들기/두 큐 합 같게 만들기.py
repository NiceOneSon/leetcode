from collections import deque
def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    answer = 0
    for _ in range(2*(len(queue1) + len(queue2))):
        if sum1 == sum2:
            break
        elif sum1 > sum2:
            popped = queue1.popleft()
            queue2.append(popped)
            sum1 -= popped
            sum2 += popped
        else:
            popped = queue2.popleft()
            queue1.append(popped)
            sum2 -= popped
            sum1 += popped
        answer += 1
        
    if sum1 != sum2:
        return -1
            
    
    return answer