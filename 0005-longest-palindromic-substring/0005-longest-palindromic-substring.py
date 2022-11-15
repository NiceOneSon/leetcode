class Solution:
    def longestPalindrome(self, s: str) -> str:
        i,l=0,0
        for j in range(len(s)):
            if s[j-l:j+1] == s[j-l:j+1][::-1]:
                l += 1
            elif j-l-1 >= 0 and s[j-l-1:j+1] == s[j-l-1:j+1][::-1]:
                l += 2
            else:
                continue
            i = j + 1
        return s[i-l:i]