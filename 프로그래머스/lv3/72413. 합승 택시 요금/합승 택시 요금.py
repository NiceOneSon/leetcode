import heapq

def solution(n, s, a, b, fares):
    answer = 0
    INF = float('inf')
    routes = [[INF] * (n+1) for _ in range(n+1)]
    
    def dijkstra():
        q = []
        for i in range(n+1):
            routes[i][i] = 0
        
        for a, b, cost in fares:
            routes[a][b] = cost
            routes[b][a] = cost
        for s in range(1, n+1):
            for t in range(1, n+1):
                if s == t:
                    continue
                if routes[s][t] != INF:
                    heapq.heappush(q, (routes[s][t], s, t))
        
                
        while q:
            cost, s, t = heapq.heappop(q)
            for othernode in range(1, n+1):
                if routes[s][othernode] > cost + routes[t][othernode]:
                    heapq.heappush(q, (cost + routes[t][othernode], s, othernode))
                    routes[s][othernode] = cost + routes[t][othernode]
                    routes[othernode][s] = cost + routes[t][othernode]
                    
                
        return routes
    
    routes = dijkstra()
    answer = routes[s][a]+routes[s][b]
    for node in range(1, n+1):
        answer = min(answer, routes[s][node] + routes[node][a] + routes[node][b])
    
    return answer