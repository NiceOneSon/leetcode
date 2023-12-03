class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        numToString: dict[str, str] = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
            
            
        def dfs(idx: int, result: Optional[list[str]]) -> list[str]:
            if idx >= len(digits):
                return result
            
            if not result:
                for string in numToString[digits[idx]]:
                    result.append(string)
                return dfs(idx + 1, result)
            
            else:
                tmpResult = []
                for string in numToString[digits[idx]]:
                    for resultString in result:
                        tmpResult.append(resultString + string)
                return dfs(idx + 1, tmpResult)
            
            
        return dfs(0, [])
                
            