import heapq

def solution(n, roads, sources, destination):
    answer = []
    INF = float('inf')
    nodes = [[] for i in range(n+1)]
    for st, en in roads:
        nodes[st].append(en)
        nodes[en].append(st)
    
    routes = [INF] * (n+1)
    routes[destination] = 0
    q = []
    for node in nodes[destination]:
        routes[node] = 1
        q.append((1, node))
    
    def dijkstra(start, routes, q):
        while q:
            cost, node = heapq.heappop(q)
            for nextnode in nodes[node]:
                if cost + 1 < routes[nextnode]:
                    routes[nextnode] = cost + 1
                    heapq.heappush(q, (cost + 1, nextnode))
        return routes
    result = dijkstra(destination, routes, q)
    # routes 만듬 (1차원), 인접행렬 거리 1 세팅
    # q에 넣고 dijkstra
    return [result[source] if result[source] != INF else -1 for source in sources]