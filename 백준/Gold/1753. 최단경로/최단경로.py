import sys
import heapq


sys.setrecursionlimit(10 ** 9)
read = sys.stdin.readline
def write(*args):
    for arg in args:
        sys.stdout.write(str(arg))


def solve():
    V, E = map(int, read().split())
    K = int(read())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, read().split())
        graph[u].append((w, v))

    INF = int(1e9)
    
    costs = [INF for _ in range(V + 1)]
    costs[K] = 0
    q = []
    heapq.heappush(q, (0, K))
    while q:
        cost, node = heapq.heappop(q)
        if (costs[node] < cost):
            continue
        for nc, nn in graph[node]:
            total = nc + cost
            if (total < costs[nn]):
                costs[nn] = total
                heapq.heappush(q, (total, nn))

    write('\n'.join(map(lambda x: 'INF' if (x == INF) else str(x), costs[1:])))


if __name__ == '__main__':
    solve()