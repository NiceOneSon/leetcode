class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        answer = 0 
        q = []
        
        for right in range(len(neededTime)):
            if not q:
                q.append(right)
                continue
                
            left = q[-1]
            if colors[left] != colors[right]:
                q.append(right)                
            
            elif neededTime[left] < neededTime[right]:
                answer += neededTime[left]
                q[-1] = right
                
            
            elif neededTime[left] >= neededTime[right]:
                answer += neededTime[right]
                      
        return answer

