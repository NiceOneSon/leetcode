
N = int(input())
length = 101
routes = [[False] * length for i in range(length)]
answer = 0
dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]
# 동북서남
# 서 -> 남
# 남 -> 동
# 동 -> 북
# 북 -> 서
# 남 동 -> 동 북

def make_dragon(routes, y, x, direction):
    tmp = []
    for i in range(len(direction)-1, -1, -1):
        d = direction[i]
        newd = ((d+2)%4 + 1)%4
        sy, sx = y+dy[newd], x+dx[newd]
        routes[sy][sx] = True
        y, x = sy, sx
        tmp.append((newd+2) % 4)
    direction += tmp
    return y, x

for i in range(N):
    x, y, d, g = map(int, input().split(' '))
    direction = []
    sy, sx = y+dy[d], x+dx[d]
    routes[y][x] = True
    routes[sy][sx] = True
    y, x = sy, sx
    direction.append((d+2)%4)
    for i in range(g):
        y, x = make_dragon(routes, y, x, direction)

for y in range(length-1):
    for x in range(length-1):
        if routes[y][x] and routes[y+1][x] and routes[y][x+1] and routes[y+1][x+1]:
            answer += 1
print(answer)