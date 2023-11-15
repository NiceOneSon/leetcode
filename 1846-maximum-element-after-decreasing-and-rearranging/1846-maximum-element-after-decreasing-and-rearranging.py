import heapq

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        q = arr 
        heapq.heapify(q)
        answer = [1]
        heapq.heappop(q)
        
        
        while q:
            value = heapq.heappop(q)
            if abs(value - answer[-1]) > 1:
                answer.append(answer[-1] + 1)
            else:
                answer.append(value)
        return max(answer)
            