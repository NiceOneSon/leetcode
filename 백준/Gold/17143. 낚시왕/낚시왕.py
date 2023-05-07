from itertools import combinations

R, C, M = map(int, input().split(' '))

routes = [[None] * (C+1) for __ in range(R+1)]

dy, dx = (0, -1, 1, 0, 0), (0, 0, 0, 1, -1)


for _ in range(M):
    r, c, z, d, s = map(int, input().split(' ')) # s : 크기, d : 이동방향, z : 속도
    routes[r][c] = (s, z, d)


def getfish(col):
    for row in range(1, R+1):
        if routes[row][col] != None:
            s, *_ = routes[row][col]
            routes[row][col] = None
            return s
    return 0

def coordinate(sy, sx, i):
    if sy < 1:
        sy = abs(sy - 1) + 1
        i = 2

    elif sy > R:
        sy = R - (sy - R)
        i = 1

    elif sx < 1:
        sx = abs(sx - 1) + 1
        i = 3

    elif sx > C:
        sx = C - (sx - C)
        i = 4
    return sy, sx, i 

def moveshark():
    tmp = [[None] * (C+1) for __ in range(R+1)]
    for y in range(1, R+1):
        for x in range(1, C+1):
            if routes[y][x]:
                i_s, i_z, i = routes[y][x]
                s, z = i_s, i_z
                if i <= 2:
                    z %= (2 * R - 2)
                else:
                    z %= (2 * C - 2)
                
                # move
                sy, sx = y + dy[i] * z, x + dx[i] * z
                
                # coordinate
                while not(1<=sy<=R and 1<=sx<=C):
                    sy, sx, i = coordinate(sy, sx, i)

                if tmp[sy][sx]:
                    comp_s, *_ = tmp[sy][sx]
                    if comp_s > s: # eat small shark
                        continue
                tmp[sy][sx] = (s, i_z, i)
    return tmp


answer = 0

for column in range(1, C+1):
    result = getfish(column)
    answer += result
    # print('beforemove')
    # [print(row) for row in routes]
    
    routes = moveshark()
    # print('aftermove')
    # [print(row) for row in routes]
    

print(answer)

