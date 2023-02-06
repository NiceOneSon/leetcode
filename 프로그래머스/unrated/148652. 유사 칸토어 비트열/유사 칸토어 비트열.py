def solution(n, l, r):
    if n == 0:
        return 1
    if l > 1:
        return solution(n, 0, r) - solution(n, 0, l-1)
    
    if r <= (5 ** (n-1)):
        return solution(n-1, 0, r)
    elif r <= (2 * 5 ** (n-1)):
        return 1 * 4 ** (n-1) + solution(n-1, 0, r - 1 * 5**(n-1))
    elif r <= (3 * 5 ** (n-1)):
        return 2 * 4 ** (n-1)
    elif r <= (4 * 5 ** (n-1)):
        return 2 * 4 ** (n-1) + solution(n-1, 0, r - 3 * 5**(n-1))
    else:
        return 3 * 4 ** (n-1) + solution(n-1, 0, r - 4 * 5**(n-1))
    