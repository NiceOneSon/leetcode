class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        from collections import defaultdict
        n = defaultdict(bool)
        for num in arr:
            n[num] = True
        
        answer = 0
        
        from functools import lru_cache
        
        @lru_cache(None)
        def top_down(parent):
            result = 1
            
            for num in arr:
                if num >= parent:
                    break
                if parent % num:
                    continue
                isOther = n[parent // num]
                if isOther:
                    tmp = 1
                    tmp *= top_down(num)
                    tmp *= top_down(parent//num)
                    result += tmp 
            return result
        
        for num in arr[::-1]:
            answer += top_down(num)
        return answer % (10**9 + 7)