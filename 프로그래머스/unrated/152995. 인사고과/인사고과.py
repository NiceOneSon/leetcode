def solution(scores):
    answer = 1
    score = sum(scores[0])
    hoA, hoB = scores[0]
    scores.sort(key = lambda x : (-x[0], x[1]))
    
    _, maxB = scores[0]
    
    for A, B in scores:
        if maxB <= B:
            if score < A + B:
                answer += 1
            maxB = B
            if hoA < A and hoB < B:
                return -1
        else:
            continue
    
    return answer