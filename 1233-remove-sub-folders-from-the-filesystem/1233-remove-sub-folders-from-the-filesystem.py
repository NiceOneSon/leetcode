from collections import defaultdict

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()
        
        stack = []
        def is_same(f: string):
            _f = stack[-1]
            f_s = f.split("/")
            _f_s = _f.split("/")
            for i in range(min(len(f_s), len(_f_s))):
                if f_s[i] != _f_s[i]:
                    return False
            return True
        
        for f in folders:
            if not stack:
                stack.append(f)
                continue
            
            if is_same(f):
                continue
                
            stack.append(f)
            
        return stack
