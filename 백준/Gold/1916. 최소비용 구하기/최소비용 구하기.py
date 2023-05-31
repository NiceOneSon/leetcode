import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = float('inf')
infos = [set() for _ in range(N+1)]
d = defaultdict(lambda : INF)

q = []
for _ in range(M):
    fcity, tcity, cost = map(int, input().split(' '))
    if cost < d[(fcity, tcity)]:
        d[(fcity, tcity)] = cost
        infos[fcity].add(tcity)

fcity, _tcity = map(int, input().split(' '))
fcity, tcity = fcity, _tcity
for city in infos[fcity]:
    heapq.heappush(q, (d[(fcity, city)], city))

while q:
    cost, city = heapq.heappop(q)
    if d[(fcity, city)] < cost:
        continue
    for nextcity in infos[city]:
        _cost = d[(city, nextcity)]
        newcost = cost + _cost
        if d[(fcity, nextcity)] > newcost:
            d[(fcity, nextcity)] = newcost
            heapq.heappush(q, (newcost, nextcity))

print(d[(fcity, _tcity)])