def solution(n):
    routes = [[] for i in range(n+1)]
    routes[1] = ['()']
    
    for i in range(2, n+1):
        s = set()
        for string in routes[i-1]:
            s.add('(' + string + ')')
        
        for x in range(1, i):
            y = i - x
            for xstring in routes[x]:
                for ystring in routes[y]:
                    s.add(xstring + ystring)
                    s.add(ystring + xstring)
        routes[i] = list(s)
        
    return len(routes[-1])
    