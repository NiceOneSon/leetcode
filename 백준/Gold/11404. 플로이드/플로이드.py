import sys

input = sys.stdin.readline

cities = int(input())

buses = int(input())

INF = float('inf')

dp = [[INF] * (cities+1) for _ in range(cities+1)]

for _ in range(buses):
    c1, c2, cost = map(int, input().split(' '))
    dp[c1][c2] = min(dp[c1][c2], cost)
    # dp[c2][c1] = min(dp[c2][c1], cost)

for city in range(1, cities+1):
    dp[city][city] = 0

def dijkstra():
    import heapq
    q = []
    for S in range(1, cities+1):
        for E in range(1, cities+1):
            if dp[S][E] != INF:
                heapq.heappush(q, (dp[S][E], S, E))

    while q:
        cost, S, E = heapq.heappop(q)
        for _E in range(1, cities+1):
            if dp[S][_E] > cost + dp[E][_E]:
                dp[S][_E] = cost + dp[E][_E]
                heapq.heappush(q, (dp[S][_E], S, _E))
dijkstra()

for city1 in range(1, cities+1):
    for city2 in range(1, cities+1):
        if dp[city1][city2] == INF:
            dp[city1][city2] = 0

for row in dp[1:]:
    print(*row[1:])
