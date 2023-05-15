
import sys
input = sys.stdin.readline

R, C = map(int, input().split(' '))

dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

routes = [list(input()) for _ in range(R)]
dupli = set()
answer = 0
def dfs(y, x):
    global answer
    dupli.add(routes[y][x])
    answer = max(answer, len(dupli))
    for i in range(4):
        sy, sx = y+dy[i], x+dx[i]
        if not(0<=sy<R and 0<=sx<C):
            continue
        if routes[sy][sx] in dupli:
            continue
        dfs(sy, sx)
    dupli.remove(routes[y][x])

dfs(0, 0)
print(answer)
