class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        for ind, row in enumerate(mat):
            cnt = 0
            for val in row:
                if val:
                    cnt += 1
            arr.append((cnt, ind))
        
        arr.sort()
        extract_index = list(map(lambda x : x[1], arr))
        
        return extract_index[:k]
            