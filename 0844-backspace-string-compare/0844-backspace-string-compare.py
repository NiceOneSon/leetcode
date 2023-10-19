class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getResult(s):
            stack = []
            for string in s:
                if string != '#':
                    stack.append(string)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        
        s = getResult(s)
        t = getResult(t)
        return s == t
                    