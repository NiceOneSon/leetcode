class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        import heapq
        
        q = [(-nums[0], 0)]
        
        answer = nums[0]
        
        for i in range(1, len(nums)):
            while i - q[0][1] > k:
                heapq.heappop(q)
            
            curr = max(0, -q[0][0]) + nums[i]
            answer = max(answer, curr)
            heapq.heappush(q, (-curr, i))
        
        return answer