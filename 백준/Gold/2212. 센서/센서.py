N = int(input())

K = int(input())

routes = list(map(int, input().split(' ')))

routes.sort()

routes = [routes[i] - routes[i-1] for i in range(1, len(routes))]

routes.sort(reverse=True)

print(sum(routes[K-1:]))
