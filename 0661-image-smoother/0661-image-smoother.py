class Solution:
    def getPoint(self, y: int, x: int, img: List[List[int]]) -> int:
        total = 0
        cnt = 0
        
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                sy, sx = y + dy, x + dx
                if not (0<=sy<len(img)) or not (0<=sx<len(img[0])):
                    continue
                cnt += 1
                total += img[sy][sx]
        return total // cnt
        
        
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        answer = []
        for y in range(len(img)):
            row = []
            for x in range(len(img[0])):
                point = self.getPoint(y, x, img)
                row.append(point)
            answer.append(row)
        return answer 