class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        from collections import defaultdict
        
        word_dict = defaultdict(int)
        
        for source_string in s:
            word_dict[source_string] += 1
        
        for target_string in t:
            word_dict[target_string] -= 1
            if word_dict[target_string] < 0:
                return False
        
        return True
        