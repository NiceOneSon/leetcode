def solution(n):
    answer = 0
    return (n // 7) + (1 if n % 7 else 0)