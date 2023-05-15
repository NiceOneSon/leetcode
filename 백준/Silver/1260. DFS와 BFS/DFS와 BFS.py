N, M, V = map(int, input().split(' '))

routes = [[] for _ in range(N+1)]
S, E = None, None
orders = []

for _ in range(M):
    n1, n2 = map(int, input().split(' '))
    if S == None and E == None:
        S = n1
        E = n2
    routes[n1].append(n2)
    routes[n2].append(n1) # 인접 리스트
    orders.append((n1, n2))

def getvisited(N):
    visited = [False] * (N+1)
    return visited

def getdfs(S, visited):
    result = False
    answer = []
    for node in routes[S]:
        if visited[node]:
            continue
        visited[node] = True
        result = True
        answer.append(node)
        answer.extend(getdfs(node, visited))
    if result == False:
        return []
    return answer

def getbfs(S, visited):
    from collections import deque
    q = deque()
    q.append(S)
    visited[S] = True
    answer = []
    while q:
        S = q.popleft()
        for node in routes[S]:
            if visited[node]:
                continue
            visited[node] = True
            q.append(node)
            answer.append(node)
    return answer


for node in range(N+1):
    routes[node].sort()

visited = getvisited(N)
visited[V] = True
answer = [V] + getdfs(V, visited)
print(*answer)

visited = getvisited(N)
visited[V] = True
answer = [V] + getbfs(V, visited)
print(*answer)