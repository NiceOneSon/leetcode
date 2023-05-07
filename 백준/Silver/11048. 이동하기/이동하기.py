r, c  = map(int, input().split())
routes = list(map(int, input().split()))
for x in range(1,c):
    routes[x] += routes[x-1]
for _ in range(r-1):
    row = list(map(int, input().split()))
    row[0] += routes[0]
    for x in range(1, c):
        row[x] += max(row[x-1], routes[x])
    routes = row
print(routes[-1])