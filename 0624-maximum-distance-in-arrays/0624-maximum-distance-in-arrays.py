class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        g_min_val, g_max_val = arrays[0][0], arrays[0][-1]
        answer = -1
        for idx in range(1, len(arrays)):
            array = arrays[idx]
            min_val, max_val = array[0], array[-1]
            l_max_distance = max(abs(max_val-g_min_val), abs(min_val-g_max_val))
            answer = max(answer, l_max_distance)
            g_min_val, g_max_val = min(g_min_val, min_val), max(g_max_val, max_val)
        return answer
