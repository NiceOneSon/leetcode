from collections import deque
import sys

input = sys.stdin.readline

def getRow():
    inserted = input().split(' ')
    if not inserted[-1]:
        inserted.pop()
    return list(map(int, inserted))

T = int(input())
INF = float('inf')

def topology(N, K, routes):

    nodes = [[] for _ in range(N+1)]
    ingress = [0] * (N+1)
    DP = [0] * (N+1)
    q = deque()

    for _ in range(K):
        b1, b2 = getRow()
        ingress[b2] += 1
        nodes[b1].append(b2)
    
    for b in range(1, N+1):
        if ingress[b] == 0:
            DP[b] = routes[b]
            q.append(b)
    
    while q:
        b = q.popleft()
        for otherb in nodes[b]:
            ingress[otherb] -= 1
            DP[otherb] = max(DP[otherb], DP[b] + routes[otherb])
            if ingress[otherb] == 0:
                q.append(otherb)
    return DP


for i in range(T):
    result = getRow()
    N, K = result
    routes = [0] + getRow()
    DP = topology(N, K, routes)
    print(DP[int(input())])
