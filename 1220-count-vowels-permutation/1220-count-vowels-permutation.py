class Solution:
    def countVowelPermutation(self, goal: int) -> int:
        
        
        def recur(a, e, i, o, u, n):
            if n == 1:
                return a + e + i + o + u
            
            ta = e + i + u
            te = a + i
            ti = e + o
            to = i
            tu = o + i
            
            return recur(ta, te, ti, to, tu, n - 1) % (10**9 + 7)
    
        return recur(1, 1, 1, 1, 1, goal)