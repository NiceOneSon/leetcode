import sys
import copy
input = sys.stdin.readline

N = int(input())
routes = [list(map(int, input().split(' '))) for _ in range(N)]

def move(routes, direction):
    changed = False
    result = 0
    if direction == 1:
        for x in range(len(routes)):
            q = []
            for y in range(len(routes)):
                if routes[y][x]:
                    if q and q[-1][1] == False:
                        if q[-1][0] == routes[y][x]:
                            q[-1][1] = True
                            q[-1][0] *= 2
                            continue
                    result = max(result, routes[y][x])
                    q.append([routes[y][x], False])
            if len(routes)!=len(q):
                changed = True
            
            for y in range(len(routes)):
                if y < len(q):
                    routes[y][x] = q[y][0]
                else:
                    routes[y][x] = 0
                        
                
    elif direction == 2:
        for x in range(len(routes)):
            q = []
            for y in range(len(routes)-1, -1, -1):
                if routes[y][x]:
                    if q and q[-1][1] == False:
                        if q[-1][0] == routes[y][x]:
                            q[-1][1] = True
                            q[-1][0] *= 2
                            continue
                    result = max(result, routes[y][x])
                    q.append([routes[y][x], False])
            if len(routes)!=len(q):
                changed = True

            for y in range(len(routes)-1, -1, -1):
                if len(routes) - y - 1 < len(q):
                    routes[y][x] = q[len(routes) - y - 1][0]
                else:
                    routes[y][x] = 0

    elif direction == 3:
        for y in range(len(routes)):
            q = []
            for x in range(len(routes)):
                if routes[y][x]:
                    if q and q[-1][1] == False:
                        if q[-1][0] == routes[y][x]:
                            q[-1][1] = True
                            q[-1][0] *= 2
                            continue
                    
                    result = max(result, routes[y][x])
                    q.append([routes[y][x], False])
            if len(routes)!=len(q):
                changed = True

            for x in range(len(routes)):
                if x < len(q):
                    routes[y][x] = q[x][0]
                else:
                    routes[y][x] = 0
    else:
        for y in range(len(routes)):
            q = []
            for x in range(len(routes)-1, -1, -1):
                if routes[y][x]:
                    if q and q[-1][1] == False:
                        if q[-1][0] == routes[y][x]:
                            q[-1][1] = True
                            q[-1][0] *= 2
                            continue
                    result = max(result, routes[y][x])
                    q.append([routes[y][x], False])
            if len(routes)!=len(q):
                changed = True

            for x in range(len(routes)-1, -1, -1):
                if len(routes) - x - 1 < len(q):
                    routes[y][x] = q[len(routes) - x - 1][0]
                else:
                    routes[y][x] = 0
    return changed, result


def recur(routes, cnt, answer):
    if cnt > 5:
        return answer

    for i in range(1, 5):
        tmproutes = [row[:] for row in routes]
        changed, result = move(tmproutes, i)
        if not changed:
            answer = max(answer, result)
            continue
        answer = max(answer, recur(tmproutes, cnt+1, result))

    return answer

# move(routes, 1)
# move(routes, 2)
# move(routes, 3)
# move(routes, 4)
# print(routes)
print(recur(routes, 0, 0))
# print(routes)

# 4
# 0 64 2 1024
# 2 512 8 0
# 0 32 512 256
# 64 64 8 2

# 5
# 2 0 0 0 0
# 2 0 0 0 0
# 4 0 0 0 0
# 2 0 0 0 0
# 2 0 0 0 0