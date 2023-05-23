import sys
sys.setrecursionlimit(10**6)

from functools import lru_cache

@lru_cache(1000)
def recur(depth, n):
    if depth == 1:
        return 10 - n
    answer = 0
    for i in range(n, 10):
        answer += recur(depth - 1, i)
    return answer%10007
N = int(input())
print(recur(N, 0))
