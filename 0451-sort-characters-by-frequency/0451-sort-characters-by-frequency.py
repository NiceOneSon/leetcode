from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(list(s))
        arr = [(-value, key) for key, value in counter.items()]
        arr.sort()
        return ''.join(map(lambda x : x[1]*-x[0], arr))