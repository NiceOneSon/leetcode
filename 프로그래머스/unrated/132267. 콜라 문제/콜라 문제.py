def solution(a, b, n):
    answer = 0
    while n >= a:
        give = n // a
        resi = n % a
        get = give * b
        resi += get
        answer += get
        n = resi
    return answer