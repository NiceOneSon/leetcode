class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        length=len(words)
        if length == 1:
            return True
        
        from collections import defaultdict
        
        alphabet_count = defaultdict(int)
        
        
        
        for word in words:
            for alphabet in word:
                alphabet_count[alphabet] += 1
        
        
        for cnt in alphabet_count.values():
            if cnt % length != 0:
                return False
        
        return True