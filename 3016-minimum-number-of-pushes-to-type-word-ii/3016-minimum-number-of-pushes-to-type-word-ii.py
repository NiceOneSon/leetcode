from collections import Counter
        
        
class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        infos = [(cnts, alpha) for alpha, cnts in c.items()]
        infos.sort(reverse = True)
        answer: int = 0
        
        for idx, (cnts, alpha) in enumerate(infos, start = 0):
            number = idx // 8
            number += 1
            answer += number * cnts
        return answer