class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        answer = -1
        for alphabet_idx in range(26):
            char = chr(alphabet_idx + ord('a'))
            left, right = s.find(char), s.rfind(char)
            if left == right:
                continue
            answer = max(answer, right - left - 1)
            
        return answer