from collections import defaultdict
import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]) -> None:
        self.graph = defaultdict(lambda : defaultdict(lambda : float('inf')))
        for f, t, v in edges:
            self.graph[f][t] = v
        return None
        

    def addEdge(self, edge: List[int]) -> None:
        f, t, v = edge
        self.graph[f][t] = v
        return None

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        q = []
        for other in self.graph[node1].keys():
            heapq.heappush(q, (self.graph[node1][other], other))
        while q:
            dist, node = heapq.heappop(q)
            if node == node2:
                continue
            for other in self.graph[node].keys():
                if self.graph[node1][other] > self.graph[node][other] + dist:
                    heapq.heappush(q, (self.graph[node][other] + dist, other))
                    self.graph[node1][other] = self.graph[node][other] + dist
                
                    
        if self.graph[node1][node2] == float('inf'):
            return -1
        return self.graph[node1][node2]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)