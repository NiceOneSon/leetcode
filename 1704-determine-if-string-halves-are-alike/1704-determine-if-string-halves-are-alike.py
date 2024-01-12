class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        length = len(s)
        
        left, right = s[:length//2], s[length//2:]
        
        vowels = 'aeiouAEIOU'
        
        lcnt, rcnt = 0, 0 
        
        for vowel in vowels:
            lcnt += left.count(vowel)
            rcnt += right.count(vowel)
        
        return lcnt == rcnt
            