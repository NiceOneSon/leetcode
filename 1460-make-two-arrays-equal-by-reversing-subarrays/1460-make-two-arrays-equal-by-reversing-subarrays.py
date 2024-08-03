from collections import Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        
        cnt_target: dict = Counter(target)
        cnt_arr: dict = Counter(arr)
        for number, cnt in cnt_target.items():
            if number not in cnt_arr:
                return False
            if cnt_arr[number] != cnt:
                return False
        
        return True