from collections import deque

def solution(cards):
    routes = []
    def get_route(ind):
        result = deque([])
        while cards[ind] not in result:
            result.append(cards[ind])
            ind = cards[ind] - 1
        minval = min(result)
        while result[0] != minval:
            result.append(result.popleft())
        return result
    
    def check_dupli(routes, result):
        for route in routes:
            if route == result:
                return True
        return False
    
    for ind in range(len(cards)):
        result = get_route(ind)
        if not check_dupli(routes, result):
            routes.append(result)
    
    routes.sort(key = lambda x : -len(x))

    return len(routes[0]) * len(routes[1]) if len(routes) >= 2 else 0
            
    