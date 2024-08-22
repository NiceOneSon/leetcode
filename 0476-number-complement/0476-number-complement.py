class Solution:
    def findComplement(self, num: int) -> int:
        str_n = list(str(bin(num))[2:])
        pointer = -1
        answer = 0
        while str_n:
            number = str_n.pop()
            pointer += 1
            if number == '1':
                continue
            answer += 2 ** pointer
            
        return answer