from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = defaultdict(int)
        for string in s[::-1]:
            d[string] += 1
        
        stack = []
        
        
        for string in s:
            if not stack:
                stack.append(string)
                d[string] -= 1
            
            elif string in stack:
                d[string] -= 1
                continue
            
            else:
                while stack and stack[-1] > string and d[stack[-1]] > 0:
                    stack.pop()
                else:
                    stack.append(string)
                    d[string] -= 1
        
        return ''.join(stack)