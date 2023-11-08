class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int, moved = False) -> bool:
        
        if sx > fx: # left to right
            return self.isReachableAtTime(fx, fy, sx, sy, t, moved = moved)
        
        if t < 0:
            return False
        elif sx == fx and sy == fy and (moved == False and t == 1):
            return False
        elif sx == fx and sy == fy and t >= 0:
            return True
        
        if sx != fx and sy != fy:
            distance = min(abs(sx - fx), abs(sy - fy))
            if sy < fy:
                return self.isReachableAtTime(sx + distance, sy + distance, fx, fy, t - distance, moved = True)
            else:
                return self.isReachableAtTime(sx + distance, sy - distance, fx, fy, t - distance, moved = True)
        else:
            distance = max(abs(sx - fx), abs(sy - fy))
            return self.isReachableAtTime(fx, fy, fx, fy, t - distance, moved = True)