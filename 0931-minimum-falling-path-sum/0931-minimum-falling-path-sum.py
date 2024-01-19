class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        y, x = len(matrix), len(matrix[0])
        
        answer = [[float('inf')] * x for _ in range(y)]
        
        min_idx = 0
        row = matrix[0]
        for i in range(x):
            answer[0][i] = row[i]
        
        
        
        dy, dx = (-1, -1, -1), (-1, 0, 1)
        for yi in range(1, y):
            for xi in range(x):
                for i in range(3):
                    sy, sx = yi + dy[i], xi + dx[i]
                    
                    if not (0<=sx<x):
                        continue
                    # print(answer[yi][xi], matrix[yi], yi, xi, sy, sx)
                    answer[yi][xi] = min(answer[yi][xi], matrix[yi][xi] + answer[sy][sx])
        
        return min(answer[-1])
        