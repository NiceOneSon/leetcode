class Solution:
    
    def checkIsSpecial(self, y: int, x: int, mat: List[List[int]]) -> int:
        answer = True
        cnt = 0
        for xtmp in range(len(mat[0])):
            if mat[y][xtmp]:
                cnt += 1
        
        for ytmp in range(len(mat)):
            if mat[ytmp][x]:
                cnt += 1
        
        if cnt == 2:
            return 1
        return 0
            
    
    def numSpecial(self, mat: List[List[int]]) -> int:
        ylen, xlen = len(mat), len(mat[0])
        
        answer = 0
        
        for y in range(ylen):
            for x in range(xlen):
                if mat[y][x]:
                    answer += self.checkIsSpecial(y, x, mat)
                    
        
        return answer