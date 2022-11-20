from collections import Counter
def solution(N, stages):
    answer = []
    length = len(stages)
    count = Counter(stages) 
    
    for i in range(1, N+1):
        if i in count:
            answer.append(count[i]/length)
            length -= count[i]
        else:
            answer.append(0)
            
    return list(zip(*sorted(enumerate(answer, start = 1), key = lambda x :(-x[1], x[0]))))[0]