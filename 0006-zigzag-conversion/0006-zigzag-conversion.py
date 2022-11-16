class Solution:
    def convert(self, s: str, numRows: int) -> str:
        routes = [''] * numRows
        ind = 0
        answer = ''
        r, c, down = 0, 0, True
        
        if numRows == 1:
            return s
        while ind < len(s):
            routes[r] += s[ind]
            ind += 1
            if down:
                if r == numRows-1:
                    down = False
                    r -= 1
                else:
                    r += 1

            elif not down:
                if r == 0:
                    down = True
                    r += 1
                else:
                    r -= 1
        return ''.join(routes)