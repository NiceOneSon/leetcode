class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        dp = [pref[0]]

        for val1, val2 in zip(pref[:-1], pref[1:]):
            dp.append(val1^val2)
            
        return dp
      
    
#         prev 1 0 1
        
#         pref 0 1 0
        
#         output 1 1 1 (7)
        
        
        
#         prev 0 1 0
        
#         pref 0 0 0 1 1 1
        
#         output 0 1 0 (2)
        
        
#         prev 0 0 0
        
#         pref 0 1 1
        
#         output 0 1 1 (3)
        
        
        
#         prev 0 1 1
        
#         pref 0 0 1
        
#         output 0 1 0 (1)
        