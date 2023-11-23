import heapq

class Solution:

    def fillOutQueue(q : list) -> bool:
        left, right = heapq.heappop(q), heapq.heappop(q)
        diff = right - left

        while q:
            left, right = left, right = right, heapq.heappop(q)
            if right - left != diff:
                return False
        return True
        
        
    def fillUpQueue(fromIdx : int, toIdx : int, nums : List[int]) -> List[int]:
        q = []
        for numIdx in range(fromIdx, toIdx+1):
            heapq.heappush(q, nums[numIdx])
        return q
    
    
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        import heapq
        
        answer = []
        
        for idx in range(len(l)):

            fromIdx, toIdx = l[idx], r[idx]
            
            q = Solution.fillUpQueue(fromIdx, toIdx, nums)
            
            if len(q) == 1:
                answer.append(True)
                continue
            
            isArithmetic = Solution.fillOutQueue(q)
            answer.append(isArithmetic)
        
        return answer
            
                