class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        hash = {}
        left = 0
        answer = 1
        for i in range(len(s)):
            if s[i] in hash and hash[s[i]] >= left:
                answer = max(answer, i - left)
                left = hash[s[i]]+1
            hash[s[i]] = i
        return max(answer, i - left + 1)
        
            
            