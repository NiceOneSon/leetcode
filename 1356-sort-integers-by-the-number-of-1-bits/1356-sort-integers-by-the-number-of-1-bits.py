class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        from collections import defaultdict
        from functools import lru_cache
        
        d = defaultdict(int)
        
        @lru_cache(None)
        def getBit(number):
            if not number:
                return 0
            
            resid = number % 2 
            newNumber = number >> 1
            d[number] = getBit(newNumber) + resid
            
            return d[number]
        
        
        answer = []
        for i in range(len(arr)-1, -1, -1):
            number = arr[i]
            getBit(number)
            answer.append((d[number], number))
        answer.sort()
        return map(lambda x : x[1], answer)