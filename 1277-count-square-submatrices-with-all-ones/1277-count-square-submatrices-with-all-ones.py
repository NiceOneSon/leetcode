class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        def get_mtrx_cnt(y: int, x: int):
            
            sy, sx = y, x
            length = 0
            cnt = 0
            while True:
                ey, ex = sy+length, sx+length
                if ey >= len(matrix):
                    return cnt
                
                if ex >= len(matrix[0]):
                    return cnt
                
                for cy in range(sy, sy+length+1):
                    if not matrix[cy][ex]:
                        return cnt
                
                for cx in range(sx, sx+length+1):
                    if not matrix[ey][cx]:
                        return cnt
                length += 1
                cnt += 1
        answer = 0 
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                cnt = get_mtrx_cnt(y, x)
                answer += cnt
                
        return answer