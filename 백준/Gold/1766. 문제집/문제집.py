import sys
from collections import deque
import heapq

input = sys.stdin.readline

N, M = map(int, input().split(' '))

routes = [[] for i in range(N+1)]

ingress = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split(' '))
    ingress[b] += 1
    routes[a].append(b)

for i in range(1, N+1):
    if routes[i]:
        routes[i].sort(reverse = True)

def topologySort():
    result = []
    q = []

    for i in range(1, N+1):
        if ingress[i] == 0:
            heapq.heappush(q, i)

    while q:
        node = heapq.heappop(q)
        result.append(node)
        for nextnode in routes[node]:
            ingress[nextnode] -= 1
            if ingress[nextnode] == 0:
                heapq.heappush(q, nextnode)
    return result

result = topologySort()
print(*result)

