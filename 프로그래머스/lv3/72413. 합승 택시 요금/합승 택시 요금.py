# import heapq

# def solution(n, s, a, b, fares):
#     answer = 0
#     INF = float('inf')
#     routes = [[INF] * (n+1) for _ in range(n+1)]
    
#     def dijkstra():
#         q = []
#         for i in range(n+1):
#             routes[i][i] = 0
        
#         for a, b, cost in fares:
#             routes[a][b] = cost
#             routes[b][a] = cost
#         for s in range(1, n+1):
#             for t in range(1, n+1):
#                 if s == t:
#                     continue
#                 if routes[s][t] != INF:
#                     heapq.heappush(q, (routes[s][t], s, t))
        
                
#         while q:
#             cost, s, t = heapq.heappop(q)
#             for othernode in range(1, n+1):
#                 if routes[s][othernode] > cost + routes[t][othernode]:
#                     heapq.heappush(q, (cost + routes[t][othernode], s, othernode))
#                     routes[s][othernode] = cost + routes[t][othernode]
#                     routes[othernode][s] = cost + routes[t][othernode]
                    
                
#         return routes
    
#     routes = dijkstra()
#     answer = routes[s][a]+routes[s][b]
#     for node in range(1, n+1):
#         answer = min(answer, routes[s][node] + routes[node][a] + routes[node][b])
    
#     return answer

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
import heapq
INF = int(1e7)

def solution(n, s, a, b, fares):
    answer = INF

    links = [[] for _ in range(n+1)]


    for anode, bnode, cost in fares:
        links[anode].append((cost, bnode))
        links[bnode].append((cost, anode))

    def dijkstra(start):
        dist = [INF] * (n+1)
        dist[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))

        while heap:
            cost, node = heapq.heappop(heap)

            if dist[node] < cost:
                continue

            for _cost, _node in links[node]:
                _cost += cost
                if _cost < dist[_node]:
                    dist[_node] = _cost
                    heapq.heappush(heap, (_cost, _node))
        return dist


    dp = [[]] + [dijkstra(i) for i in range(1, n+1)]
    for i in range(1, n+1):
        answer = min(answer, dp[s][i] + dp[i][b] + dp[i][a])

    return answer