from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for string in t:
            d[string] += 1
        
        
        for string in s:
            d[string] -= 1
        
        for key, val in d.items():
            if val:
                return key