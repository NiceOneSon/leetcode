class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vowels = []
        for idx in range(len(s)):
            if s[idx].lower() in 'aeiou':
                vowels.append(s[idx])
                s[idx] = None
        
        vowels.sort(reverse = True)
        
        for idx in range(len(s)):
            if s[idx] == None:
                s[idx] = vowels.pop()
        return ''.join(s)