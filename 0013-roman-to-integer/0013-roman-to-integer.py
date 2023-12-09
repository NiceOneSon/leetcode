import heapq
from typing import List

class Solution:
    def getNumber(self, minus_number: int, index: int, numbers: List[int]) -> int:
        result = -minus_number
        numbers[index] = None
        index -= 1
        
        while index >= 0 and numbers[index]:
            result -= numbers[index]
            numbers[index] = None
            
        return result
        
    
    def romanToInt(self, symbols: str) -> int:
        q = []
        answer = 0
        
        symbol_to_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10, 
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        numbers = [symbol_to_dict[symbol] for symbol in symbols]
        
        
        for index, number in enumerate(numbers):
            heapq.heappush(q, (-number, index))
        
        while q:
            minus_number, index = heapq.heappop(q)
            if numbers[index] == None:
                continue
            
            number = self.getNumber(minus_number, index, numbers)
            answer += number
        
        return answer
            
            