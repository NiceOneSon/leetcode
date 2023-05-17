from collections import deque

C, R = map(int, input().split(' '))

routes = [list(input()) for _ in range(R)]

INF = float('inf')

dp = [[[INF] * 4 for _ in range(C)] for __ in range(R)]

q = deque()

dy, dx = (-1, 1, 0, 0), (0, 0, -1 ,1)

for y in range(R):
    for x in range(C):
        if routes[y][x] == 'C':
            for i in range(4):
                sy, sx = y+dy[i], x+dx[i]
                if not(0<=sy<R and 0<=sx<C):
                    continue
                if routes[sy][sx] == '*':
                    continue
                q.append((sy, sx, 0, i)) # y, x, cnt, direction
                dp[y][x][i] = 0 
                dp[sy][sx][i] = 0
            else:
                break
    else:
        continue
    break

# init
routes[y][x]='S'
answer = INF
# limit = 1000

while q:
    # limit -= 1
    y, x, cnt, previ = q.popleft()

    for i in range(4):
        sy, sx = y+dy[i], x+dx[i]

        if not(0<=sy<R and 0<=sx<C):
            continue
        elif routes[sy][sx] == '*':
            continue

        if previ == i:
            if dp[sy][sx][i] <= cnt:
                continue
            else:
                if routes[sy][sx] == 'C':
                    answer = min(answer, cnt)
                    continue
                dp[sy][sx][i] = cnt
                q.append((sy, sx, cnt, i))
        else:
            if dp[sy][sx][i] <= (cnt + 1):
                continue
            else:
                if routes[sy][sx] == 'C':
                    answer = min(answer, cnt+1)
                    continue
                dp[sy][sx][i] = (cnt + 1)
                q.append((sy, sx, cnt+1, i))
        

        
# [print(row) for row in dp]
print(answer)