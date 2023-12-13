class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ylen, xlen = len(mat), len(mat[0])
        answer = 0
        col = [0] * xlen
        row = [0] * ylen
        
        for y in range(ylen):
            for x in range(xlen):
                if mat[y][x]:
                    col[x] += 1
                    row[y] += 1
        
        for y in range(ylen):
            for x in range(xlen):
                if mat[y][x] and col[x] == 1 and row[y] == 1:
                    answer += 1
        
        return answer