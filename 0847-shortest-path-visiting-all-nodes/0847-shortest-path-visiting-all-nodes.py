from collections import deque, defaultdict

class Solution:   
    def shortestPathLength(self, graph: List[List[int]]):
        q = deque()
        dupli = defaultdict()
        
        for i in range(len(graph)):
            dupli[i] = defaultdict(bool)
            q.append((i, 0, 1 << i)) # curr, cnt, nodes
            dupli[i][1 << i] = True
        
        
        
        
        while q:
            curr, cnt, nodes = q.popleft()
            if nodes == (1 << len(graph)) - 1:
                return cnt
            
            for i in graph[curr]:
                nextnodes = nodes | 1 << i
                if dupli[i][nextnodes]:
                    continue
                dupli[i][nextnodes] = True
                q.append((i, cnt + 1, nextnodes))
                
                
        
            