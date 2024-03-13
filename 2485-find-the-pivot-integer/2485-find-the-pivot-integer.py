class Solution:        
    def pivotInteger(self, n: int) -> int:
        def sum_range(n):
            return (n * (n+1))// 2
                
        total = sum_range(n)
        
        for i in range(1, n+1):
            if (total - i) % 2 == 0 and (total - i) // 2 == sum_range(i-1):
                return i
        
        return -1
            
    