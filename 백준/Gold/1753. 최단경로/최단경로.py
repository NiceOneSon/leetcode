import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

V, E = map(int, input().split(' '))
K = int(input())
INF = float('inf')
routes = defaultdict(lambda : INF)
routes[(K, K)] = 0
linked = defaultdict(list)
q = []

for i in range(E):
    u, v, w = map(int, input().split(' '))
    if routes[(u, v)] > w:
        routes[(u, v)] = w
        linked[u].append(v)
    if u == K:
        heapq.heappush(q, (w, v))

while q:
    cost, node = heapq.heappop(q)
    for nextnode in linked[node]:
        if routes[(K, nextnode)] > routes[(node, nextnode)] + cost:
            routes[(K, nextnode)] = routes[(node, nextnode)] + cost
            heapq.heappush(q, (routes[(K, nextnode)], nextnode))

for node in range(1, V+1):
    val = routes[(K, node)]
    if val == INF:
        print('INF')
    else:
        print(val)