N, M = map(int, input().split(' '))

routes = [list(map(int, input().split(' '))) for _ in range(N)]

# init
for i in range(1, M):
    routes[0][i] += routes[0][i-1]

def downMove(y):
    for x in range(M):
        routes[y][x] += routes[y-1][x]

def simulate(y):
    tmpL, tmpR = [0] * M, [0] * M
    tmpL[0] = routes[y-1][0] + routes[y][0]
    tmpR[-1] = routes[y-1][-1] + routes[y][-1]

    for i in range(1, M):
        tmpL[i] = max(tmpL[i-1] + routes[y][i], routes[y-1][i] + routes[y][i])
    
    for i in range(M-2, -1, -1):
        tmpR[i] = max(tmpR[i+1] + routes[y][i], routes[y-1][i] + routes[y][i])
    
    for i in range(M):
        routes[y][i] = max(tmpL[i], tmpR[i])
    # return tmp

def addToRoute(y, tmp):
    for i in range(M):
        routes[y][i] += tmp[i]

for y in range(1, N):    
    tmp = simulate(y)
    # downMove(y)
    # addToRoute(y, tmp)


# 
print(routes[-1][-1])