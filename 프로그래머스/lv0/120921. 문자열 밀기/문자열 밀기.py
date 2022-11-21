def solution(A, B):
    for i in range(len(A)):
        
        if B == A[-i:] + A[:-i]:
            return i
    return -1