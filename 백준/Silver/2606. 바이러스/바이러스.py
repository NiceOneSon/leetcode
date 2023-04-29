T = int(input())
parents = [i for i in range(T+1)]
N = int(input())

def find(p):
    if p != parents[p]:
        return find(parents[p])
    return parents[p]

def union(p1, p2):
    p1 = find(p1)
    p2 = find(p2)
    if p1 < p2:
        parents[p2] = p1
    else:
        parents[p1] = p2

for _ in range(N):
    a, b = map(int, input().split(' '))
    union(a, b)

answer = -1

for i in range(1, T+1):
    if find(i) == 1:
        answer += 1

print(max(answer, 0))