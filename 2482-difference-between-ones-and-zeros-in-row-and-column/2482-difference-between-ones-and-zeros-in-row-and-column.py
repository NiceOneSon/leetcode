class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ylen, xlen = len(grid), len(grid[0])
        
        onesRow, onesCol, zerosRow, zerosCol = [0] * ylen, [0] * xlen, [0] * ylen, [0] * xlen
        
        for y in range(ylen):
            one, zero = 0, 0
            for x in range(xlen):
                if grid[y][x] == 1:
                    one += 1
                else:
                    zero += 1
            
            onesRow[y] = one
            zerosRow[y] = zero
        
        for x in range(xlen):
            one, zero = 0, 0
            for y in range(ylen):
                if grid[y][x] == 1:
                    one += 1
                else:
                    zero += 1
            onesCol[x] = one
            zerosCol[x] = zero
        
        answer = [[0] * xlen for _ in range(ylen)]
        
        for y in range(ylen):
            for x in range(xlen):
                answer[y][x] = onesRow[y] + onesCol[x] - zerosRow[y] - zerosCol[x]
                
        return answer