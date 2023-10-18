class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        from collections import defaultdict
        from functools import lru_cache
        
        graph = defaultdict(list)
        
        for f, t in relations:
            graph[f].append(t)
        
        @lru_cache(None)
        def recursive(curr):
            if not graph[curr]:
                return time[curr-1]
            
            return time[curr-1] + max(map(recursive, graph[curr]))
        
        return max(map(recursive, range(1, n+1)))