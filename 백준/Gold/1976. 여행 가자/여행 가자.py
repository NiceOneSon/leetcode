N = int(input())
M = int(input())

parents = [i for i in range(N+1)]

def find(p):
    if p != parents[p]:
        parents[p] = find(parents[p])
    return parents[p]

def union(p1, p2):
    p1, p2 = find(p1), find(p2)

    if p1 < p2:
        parents[p2] = p1
    else:
        parents[p1] = p2


for p1 in range(N):
    row = tuple(map(int, input().split(' ')))
    for p2 in range(N):
        if row[p2]:
            union(p1, p2)

plans = tuple(map(int, input().split(' ')))
for i in range(1, M):
    if find(plans[i]-1) != find(plans[i-1]-1):
        print('NO')
        break
else:
    print('YES')