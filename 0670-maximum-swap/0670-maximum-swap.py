class Solution:
    def swap(self, q, pnts):
        for idx in range(len(q)-1, -1, -1):
            pnt = pnts[idx]
            if q[idx] < q[pnt]:
                q[idx], q[pnt] = q[pnt], q[idx]
                break
    
    def make_to_number(self, q, pnts):
        answer = 0
        for pnt in range(len(q)):
            answer += q[pnt] * 10 ** pnt
        return answer
    
    def return_maximum_value(self, q, pnts):
        self.swap(q = q, pnts = pnts)    
        return self.make_to_number(q, pnts)
        
    def maximumSwap(self, num: int) -> int:
        q = []
        pnts = []
        
        while num:
            n = num % 10
            num //= 10
            pnt = len(pnts)
            if not q:
                pnt = 0
            elif n <= q[pnts[-1]]:
                pnt = pnts[-1]
            q.append(n)
            pnts.append(pnt)
        
        return self.return_maximum_value(q, pnts)