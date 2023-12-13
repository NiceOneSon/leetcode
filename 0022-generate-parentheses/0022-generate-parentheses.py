from typing import List

class Solution:
    limit = None
    
    def recursiveGetParenthesis(self, n: int, status: int, idx: int, result: str) -> List[str]:
        if idx == Solution.limit:
            return [result]
        
        answer = []
        
        if n:
            recursive_return = self.recursiveGetParenthesis(n - 1, status + 1, idx + 1, result+'(')
            answer.extend(recursive_return)
            
        if status > 0:
            recursive_return = self.recursiveGetParenthesis(n, status - 1, idx + 1, result+')')
            answer.extend(recursive_return)
        
        return answer
        
    
    def generateParenthesis(self, n: int) -> List[str]:
        status = 0
        idx = 0
        result = ""
        Solution.limit = n * 2
        answer = self.recursiveGetParenthesis(n, status, idx, result)
        
        return answer