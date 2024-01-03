class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        left, right = None, None
        answer = 0
        for row in bank:
            cnt = row.count("1")
            if cnt == 0:
                continue
            elif right == None:
                right = cnt
            else: 
                left = right
                right = cnt
                answer += left * right
        return answer
            
            