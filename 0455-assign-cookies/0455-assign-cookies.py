import heapq

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        heapq.heapify(g)
        heapq.heapify(s)
        answer = 0 
        while s and g:
            food = heapq.heappop(s)
            if g[0] <= food:
                heapq.heappop(g)
                answer += 1
            
        return answer