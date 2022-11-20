def solution(order):
    answer = 0
    while order:
        num = order % 10
        order //= 10
        if num and num % 3 == 0:
            answer += 1
    return answer