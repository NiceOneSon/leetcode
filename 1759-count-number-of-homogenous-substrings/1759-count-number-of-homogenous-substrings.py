class Solution:
    def countHomogenous(self, s: str, same = False) -> int:
        if same == True:
            return (len(s) * (len(s) + 1))//2
        
        answer = 0
        
        left = 0
        for right in range(len(s)):
            if s[left] != s[right]:
                answer += self.countHomogenous(s[left:right], same=True)
                left = right
        
        right += 1
        answer += self.countHomogenous(s[left:right], same=True)
        return answer % (10**9 + 7)