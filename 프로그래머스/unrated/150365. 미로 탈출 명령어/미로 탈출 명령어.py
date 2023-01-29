from collections import deque

dy, dx = [1, 0, 0, -1], [0, -1, 1, 0]
template = 'dlru'

def getdistance(y, x, ty, tx):
    return abs(y - ty) + abs(x - tx)

def solution(leny, lenx, y, x, r, c, lendim):
    routes = [[''] * lenx for i in range(leny)] 
    r, c = r-1, c-1
    q = deque([(y-1, x-1, '')])
    while q:
        y, x, string = q.popleft()
        if len(string) == lendim:
            continue
        elif len(string) + getdistance(y, x, r, c) > lendim:
            continue
        for i in range(4):
            sy, sx, = y + dy[i], x + dx[i]
            sstring = string + template[i]
            if not(0 <= sy < leny):
                continue
            if not(0 <= sx < lenx):
                continue
            if not routes[sy][sx] or sstring < routes[sy][sx] or len(sstring) > len(routes[sy][sx]) :
                routes[sy][sx] = sstring
                q.append((sy, sx, sstring))
            
    return routes[r][c] if len(routes[r][c]) == lendim else 'impossible'
