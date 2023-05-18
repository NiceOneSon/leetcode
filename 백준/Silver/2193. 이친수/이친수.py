N = int(input())
routes = [0] * (max(N+1, 3))
routes[1] = 1
routes[2] = 1
for i in range(3, N+1):
    routes[i] = routes[i-1] + routes[i-2]
print(routes[N])