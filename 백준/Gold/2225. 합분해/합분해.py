routes = [[0] * 201 for _ in range(201)]

for i in range(1, 201):
    routes[1][i] = 1
    routes[i][1] = i

for i in range(2, 201):
    for j in range(2, 201):
        routes[i][j] = routes[i][j-1] + routes[i-1][j]
n, k = map(int, input().split(' '))

print(routes[k][n] % 1000000000)
# 숫자 2개 사용해서 6이면