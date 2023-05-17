import sys

input = sys.stdin.readline

N = int(input())

K = int(input())

parents = [i for i in range(N+1)]

def find(p):
    if p != parents[p]:
        parents[p] = find(parents[p])
    return parents[p]

def union(p1, p2):
    p1 = find(p1)
    p2 = find(p2)
    if p1 < p2:
        parents[p2] = p1
    else:
        parents[p1] = p2

answer = 0
skip = False
for _ in range(K):
    p = int(input())
    if skip:
        continue
    doc = find(p)
    if doc == 0:
        skip = True
    else:
        parents[doc] = parents[doc-1]
        answer += 1
print(answer)