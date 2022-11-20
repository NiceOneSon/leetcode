from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
answer = 0

def dfs(node, visited, routes):
    visited[node] = True
    global answer

    child = [nextnode for nextnode in routes[node] if visited[nextnode] == False]

    if not child:
        return True, False

    needs, brights = False, False

    for nextnode in child:
        need, bright = dfs(nextnode, visited, routes)
        needs |= need
        brights &= bright

    # 자식이 하나라도 켜달라고 할 경우
        # 부모는 등대 O, 부모는 return 시 킬 필요 없다고 전달
    # 자식이 하나라도 등대인 경우
        # 부모는 등대 X, 부모는 return 시 킬 필요 없다고 전달
    # 자식이 등대가 아닌데 킬 필요 없다고 하는 경우
        # 부모는 등대 X, 부모 return 시 켜달라고 요청.

    if needs:
        answer += 1
        return False, True
    if brights:
        return False, False
    return True, False

def solution(n, lighthouse):
    root = 2
    routes = [[] for i in range(n+1)]
    for a, b in lighthouse:
        routes[a].append(b)
        routes[b].append(a)
    visited = defaultdict(bool)
    dfs(root, visited, routes)
    return answer
