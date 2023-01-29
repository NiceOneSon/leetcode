def solution(x, y, n):
    INF = float('inf')
    routes = [INF] * (y+1)
    cnt = 0
    routes[x] = 0
    for num in range(x, y+1):
        tmp = num + n
        if tmp <= y:
            routes[tmp] = min(routes[tmp], routes[num] + 1)
        tmp = num * 2
        if tmp <= y:
            routes[tmp] = min(routes[tmp], routes[num] + 1)
        tmp = num * 3
        if tmp <= y:
            routes[tmp] = min(routes[tmp], routes[num] + 1)
    return routes[y] if routes[y] != INF else -1
        
    