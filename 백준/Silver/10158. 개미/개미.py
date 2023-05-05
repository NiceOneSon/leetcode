R, C = map(int, input().split(' '))

y, x = map(int, input().split(' '))
t = int(input())
dy, dx = (-1, 1), (-1, 1)
yi, xi = 1, 1

# 왔다 갔다 하는 게 반복
    # yn = t // R
    # if yn % 2 == 1라면 y에서 -cnt 0이라면 0에서 cnt

ymove = t % (2*(R))
xmove = t % (2*(C))

while ymove:
    sy = y + dy[yi]
    if not(0<=sy<=R):
        yi += 1
        yi %= 2
        continue
    ymove -= 1
    y = sy

while xmove:
    sx = x + dx[xi]
    if not(0<=sx<=C):
        xi += 1
        xi %= 2
        continue
    xmove -= 1
    x = sx

print(y, x)
