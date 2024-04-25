from functools import lru_cache

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        def is_distance_okay(a: int, b: int) -> bool:
            a_num = a
            b_num = b
            
            if max(a_num, b_num) - min(a_num, b_num) > k:
                return False
            return True
        
        def get_alpha_idx(character: str) -> int:
            return ord(character) - ord('a')
        
        alpha_length = ord('z') - ord('a') + 1
        
        DP = [[0] * alpha_length for _ in range(len(s))]
        DP[0][ord(s[0]) - ord('a')] = 1
        
        for idx in range(1, len(s)):
            now_alpha_idx = get_alpha_idx(s[idx])
            
            for alpha_idx in range(alpha_length):
                DP[idx][alpha_idx] = max(DP[idx-1][alpha_idx], DP[idx][alpha_idx])
                if is_distance_okay(alpha_idx, now_alpha_idx):
                    DP[idx][now_alpha_idx] = max(DP[idx-1][alpha_idx] + 1, DP[idx][now_alpha_idx])
        
        return max(DP[-1])
                # 그냥 거기서 다시 시작할 경우
                
                # compare idx와 alpha idx가 서로 다른 알파벳일 때
                    # k이하 값을 갖고와서 + 1
                     
                # " 같은 알파벳일 때
                 
                
        
# # 1 a
# # 2 b
# # 3 c
# # 4 d
# # 5 e
# # 6 f
# # 7 g
# # 8 h
# # 9 i
# # 10 j
# # 11 k
# # 12 l
# # 13 m
# # 14 n
# # 15 o
# # 16 p
# # 17 q
# # 18 r
# # 19 s
# # 20 t
# # 21 u
# # 22 v
# # 23 w
# # 24 x
# # 25 y
# # 26 z
    