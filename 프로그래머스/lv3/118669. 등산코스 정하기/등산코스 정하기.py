import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    INF = float('inf')
    q = []
    peak = defaultdict(bool)
    answer = [0, INF]
    connection = [[] for i in range(n+1)]
    routes = [INF] * (n+1)
    
    for gate in gates:
        routes[gate] = 0
    
    for summit in summits:
        peak[summit] = True
    
    for fnode, tnode, cost in paths:
        connection[fnode].append((cost, tnode))
        connection[tnode].append((cost, fnode))
        if routes[fnode] == 0: # 출발 노드
            routes[tnode] = min(routes[tnode], cost)
        if routes[tnode] == 0: # 출발 노드
            routes[fnode] = min(routes[fnode], cost)
            
    for node, distance in enumerate(routes):
        if routes[node] > 0 and routes[node] != INF:
            heapq.heappush(q, (routes[node], node))
    
    def dijkstra(q):
        answer = [0, INF]
        while q:
            cost, fnode = heapq.heappop(q)
            if peak[fnode]:
                if answer[1] > routes[fnode]:
                    answer = [fnode, routes[fnode]]
                elif answer[1] == routes[fnode] and answer[0] > fnode:
                    answer = [fnode, routes[fnode]]
                continue
            if cost > answer[1] and cost > routes[fnode]:
                continue
            
            for cost_, tnode in connection[fnode]:
                if routes[tnode] > max(cost, cost_):
                    routes[tnode] = max(cost, cost_)
                    heapq.heappush(q, (routes[tnode], tnode))
        return answer
    
    return dijkstra(q)