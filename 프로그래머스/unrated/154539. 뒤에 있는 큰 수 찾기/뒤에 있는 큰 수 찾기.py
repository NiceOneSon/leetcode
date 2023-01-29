import heapq

def solution(numbers):
    q = []
    answer = [-1] * len(numbers)
    
    for ind in range(len(numbers)):
        val = numbers[ind]
        while q and q[0][0] < val:
            qval, qind = heapq.heappop(q)
            answer[qind] = val
        heapq.heappush(q, (val, ind))
    return answer