def solution(n):
    answer = 0
    while n:
        answer += 1
        while answer % 3 == 0 or ('3' in str(answer)):
            answer += 1
        n -= 1
    return answer