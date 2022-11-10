from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(a):
            if a != parent[a]:
                return find(parent[a])
            return parent[a]
    
        def union(a, b):
            a, b = find(a), find(b)
            if a != b:
                parent[b] = a
                return True
            return False
    
        nodenum = defaultdict(int)
        nodes = []
        for ind, pos1 in enumerate(points):
            nodenum[tuple(pos1)] = ind
            for pos2 in points[ind+1:]:
                nodes.append((-(abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])), tuple(pos1), tuple(pos2)))
        nodes.sort()
        
        parent = [i for i in range(len(points))]
        
        count = 0
        
        answer = 0
        
        while count < len(points) - 1:
            distance, pos1, pos2 = nodes.pop()
            if union(nodenum[pos1], nodenum[pos2]):
                count += 1
                answer -= distance
        return answer
        
    
    