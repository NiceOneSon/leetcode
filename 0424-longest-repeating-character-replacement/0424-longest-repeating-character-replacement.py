from collections import defaultdict
import heapq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def get_other(d: dict) -> tuple[int, str]:
            arr = []
            total = 0
            for alpha, cnt in d.items():
                total += cnt
                arr.append((cnt, alpha))
            arr.sort()
            maxcnt, maxalpha = arr[-1]
            return total - maxcnt, maxalpha

        left = 0
        d = defaultdict(int)
        q = []
        answer = 0
        for right in range(len(s)):
            string = s[right]
            d[string] += 1
            
            others, alpha = get_other(d)
            while others > k and left < right:
                d[s[left]] -= 1
                left += 1
                others, alpha = get_other(d)
            length = right - left + 1
            answer = max(answer, length)

        return answer 