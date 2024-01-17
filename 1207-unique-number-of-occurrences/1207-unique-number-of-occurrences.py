class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict
        
        d = defaultdict(int)
        
        for number in arr:
            d[number] += 1
            
        s = set()
        for value in d.values():
            if value in s:
                return False
            s.add(value)
        return True