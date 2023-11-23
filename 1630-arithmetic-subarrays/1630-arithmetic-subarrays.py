class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        import heapq
        
        answer = []
        
        for idx in range(len(l)):

            fromIdx, toIdx = l[idx], r[idx]
            
            q = []
            
            for numIdx in range(fromIdx, toIdx+1):
                heapq.heappush(q, nums[numIdx])
            
            if len(q) == 1:
                answer.append(True)
            
            left, right = heapq.heappop(q), heapq.heappop(q)
            diff = right - left
            while q:
                left, right = right, heapq.heappop(q)
                if right - left != diff:
                    answer.append(False)
                    break
            else:
                answer.append(True)
        
        return answer
            
                