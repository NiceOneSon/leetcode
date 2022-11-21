def solution(a, b):
    while b % 5 == 0 or b % 2 == 0:
        if b % 5 == 0:
            b //= 5
        if b % 2 == 0:
            b //= 2
    
    if b in [1, 0]:
        return 1
    if a % b == 0:
        b //= a
    if b % a == 0:
        b //= a
    if b in [1, 0]:
        return 1
    return 2
            