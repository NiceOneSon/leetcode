class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dp = [[None] * len(grid[0]) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            dp[i][0] = 0
        
        answer = 0 
        
        for cx in range(1, len(grid[0])):
            x = cx - 1
            for cy in range(len(grid)):
                
                for i in range(-1, 2):
                    y = cy + i
                    if not(y >= 0 and y < len(grid)):
                        continue
                    
                    if dp[y][x] == None:
                        continue
                    
                    if grid[cy][cx] <= grid[y][x]:
                        continue

                    if dp[cy][cx] == None:
                        dp[cy][cx] = 0
                    
                    dp[cy][cx] = max(dp[cy][cx], dp[y][x] + 1)
                    answer = max(answer, dp[cy][cx])
        return answer