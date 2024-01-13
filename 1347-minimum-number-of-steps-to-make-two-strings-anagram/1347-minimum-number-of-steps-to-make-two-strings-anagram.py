from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        word_dict = defaultdict(int)
        
        for string in s:
            word_dict[string] += 1
        
        for string in t:
            word_dict[string] -= 1
        
        answer = 0
        s = tuple(s)
        s = set(s)
        for string in s:
            if word_dict[string] > 0:
                answer += word_dict[string]
                
        return answer