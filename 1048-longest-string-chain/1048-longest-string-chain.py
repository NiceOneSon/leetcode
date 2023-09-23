from functools import lru_cache

class Solution:
    
    s = None
    @lru_cache
    def recursive(self, word, cnt):
        s = Solution.s
        answer = 0
        for i in range(len(word)):
            newword = word[:i] + word[i+1:]
            print(word, newword)
            if newword in s:
                answer = max(answer, self.recursive(newword, cnt + 1))
        if answer:
            return answer
        else:
            return cnt + 1
        

    
    def longestStrChain(self, words: List[str]) -> int:
        
        s = set(words)
        Solution.s = s
        words.sort(key = lambda x : len(x))
        
        answer = 0
        
        while words:
            word = words.pop()
            answer = max(answer, self.recursive(word, 0))
            
        return answer