import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split(' '))

q = []

for _ in range(E):
    A, B, C = map(int, input().split(' '))
    heapq.heappush(q, (C, A, B))

parent = [i for i in range(V+1)]

def find(p):
    if p != parent[p]:
        return find(parent[p])
    return parent[p]

def union(p1, p2):
    p1 = find(p1)
    p2 = find(p2)

    if p1 == p2:
        return False
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2
    return True

answer = 0
while q:
    cost, A, B = heapq.heappop(q)
    res = union(A, B)
    if res:
        answer += cost
    
print(answer)