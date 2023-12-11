from collections import defaultdict

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        number_of_count = defaultdict(int)
        threshold = len(arr) // 4
        for number in arr:
            number_of_count[number] += 1
            if number_of_count[number] > threshold:
                return number
        return answer