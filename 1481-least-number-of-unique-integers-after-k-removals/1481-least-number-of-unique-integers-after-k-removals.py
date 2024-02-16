from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        import heapq
        
        q = []
        for num, cnt in c.items():
            heapq.heappush(q, (cnt, num))
        
        while k:
            if q[0][0] <= k:
                cnt, _ = heapq.heappop(q)
                k -= cnt
                continue
            return len(q)
        
        return len(q)