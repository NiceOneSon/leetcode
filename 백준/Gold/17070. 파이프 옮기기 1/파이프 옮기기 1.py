N = int(input())

routes = []

for _ in range(N):
    arr = list(map(int, input().split(' '))) 
    tmp = []
    for val in arr:
        if val == 1:
            val = -1
        tmp.append([val, val, val])
    routes.append(tmp)

for x in range(1, N):
    if routes[0][x][0] == -1:
        break 
    routes[0][x][0] = 1

for y in range(1, N):
    for x in range(1, N):
        for i in range(3):
            if routes[y][x][i] == -1:
                break
            
            ycheck = False if routes[y-1][x][i] == -1 else True
            xcheck = False if routes[y][x-1][i] == -1 else True
            ccheck = False if routes[y-1][x][i] == -1 or routes[y][x-1][i] == -1 or routes[y-1][x-1][i] == -1 else True

            if i == 0:
                if xcheck:
                    routes[y][x][0] += routes[y][x-1][0]
                    routes[y][x][0] += routes[y][x-1][1]
            elif i == 1:
                if ccheck:
                    routes[y][x][i] += routes[y-1][x-1][0]
                    routes[y][x][i] += routes[y-1][x-1][1]
                    routes[y][x][i] += routes[y-1][x-1][2]
                    
            else:
                if ycheck:
                    routes[y][x][i] += routes[y-1][x][1]
                    routes[y][x][i] += routes[y-1][x][2]
                    

print(max(sum(routes[-1][-1]), 0))
# [print(row) for row in routes]