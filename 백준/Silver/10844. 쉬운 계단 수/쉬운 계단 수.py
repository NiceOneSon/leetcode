N = int(input())

routes = [[0] * 10 for _ in range(N+1)]

for i in range(1, 10):
    routes[1][i] = 1

for y in range(2, N+1):
    for x in range(10):
        prev, after = x-1, x+1
        if 0 <= prev < 10:
            routes[y][x] += routes[y-1][prev]
        if 0<= after < 10:
            routes[y][x] += routes[y-1][after]
print(sum(routes[-1]) % 1000000000)