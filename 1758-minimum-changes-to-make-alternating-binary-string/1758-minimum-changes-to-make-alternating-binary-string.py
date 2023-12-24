class Solution:
    def getAlternating(self, s: str, change_dict) -> int:
        result = 0
        s = list(s)
        prev = s[0]
        
        for idx in range(1, len(s)):
            if s[idx] == prev:
                s[idx] = change_dict[prev]
                result += 1
            prev = s[idx]
        return result
        
    def minOperations(self, s: str) -> int:
        change_dict = {
            "0" : "1",
            "1" : "0"
        }
        answer = self.getAlternating(s, change_dict)
        answer = min(answer, self.getAlternating(change_dict[s[0]] + s[1:], change_dict) + 1)
        
        
        return answer