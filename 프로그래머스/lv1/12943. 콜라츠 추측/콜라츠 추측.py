def solution(num):
    N = 500
    answer = 0
    while N and num != 1:
        N -= 1
        answer += 1
        if num % 2 == 0:
            num //= 2
        elif num  % 2:
            num *= 3
            num += 1
    if not N:
        return -1
    return answer