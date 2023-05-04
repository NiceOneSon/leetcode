N = int(input())
M = max(3, N)
routes = [0] * (M+1)
routes[1] = 1
routes[2] = 3
for i in range(3, M+1):
    routes[i] = routes[i-1] + 2 * routes[i-2]
print(routes[N]%10007)