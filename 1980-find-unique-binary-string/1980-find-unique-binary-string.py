class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        def getNumber(string : str) -> int:
            num = 0
            for number in string:
                num = num << 1
                num |= int(number)
            return num
        
        def getString(number : int) -> str:
            string = ''
            while number:
                resid = number % 2
                number = number >> 1
                if resid:
                    string += '1'
                else:
                    string += '0'
            while len(string) < len(nums):
                string += '0'
            return string[::-1]
        if len(nums) == 1:
            num = getNumber(nums[0])
            num = abs(num - 1)
            return getString(num)
                
        s = set()
        
        for num in nums:
            num = getNumber(num)
            s.add(num)
        
        for num in range(1, 1 << len(nums)):
            if num not in s:
                return getString(num)