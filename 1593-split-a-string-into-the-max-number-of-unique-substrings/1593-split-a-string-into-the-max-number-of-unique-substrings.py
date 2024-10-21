class Solution:
    def maxUniqueSplit(self, string: str) -> int:
        s = []
        def recur(idx):
            nonlocal s
            if idx == len(string):
                return len(set(s))
            
            if idx == 0:
                s.append(string[idx])
                return recur(idx+1)
            
            result = 0
            s.append(string[idx])
            result = max(result, recur(idx + 1))
            s.pop()
            last_s = s.pop()
            new_s = last_s + string[idx]
            s.append(new_s)
            result = max(result, recur(idx + 1))
            return result
        
        return recur(0)