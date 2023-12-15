class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from collections import defaultdict
        
        destinations = defaultdict(str)
        
        for begin, end in paths:
            destinations[begin] = end
        
        
        begin = paths[0][1]
        while destinations[begin]:
            end = destinations[begin]
            begin = end
        
        return begin
            