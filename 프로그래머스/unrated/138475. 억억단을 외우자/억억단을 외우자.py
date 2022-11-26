from math import gcd
from collections import defaultdict

def solution(e, starts):
    routes = [0] * (e+1)
    
    for i in range(1, e+1):
        for j in range(i, int(e / i)+1):
            if i != j:
                routes[i*j] += 2
            else:
                routes[i*j] += 1
        
    
    answer = []
    
    starts = [(val, ind) for ind, val in enumerate(starts)]
    starts.sort()
    limit = starts[0][0]
    peak = e
    val, i = starts.pop()
    for ind in range(e, limit-1, -1):
        if routes[peak] <= routes[ind]:
            peak = ind
        if ind == val:
            answer.append((i, peak))
            if starts:
                val, i = starts.pop()
            else:
                break
    answer.sort()
    return [val for _, val in answer]