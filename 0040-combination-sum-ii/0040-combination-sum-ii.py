class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer: set = set()
        
        def recur(idx: int, arr: list[int], remain: int):
            if idx >= len(candidates):
                return
            
            if remain > candidates[idx]:
                arr.append(candidates[idx])
                recur(idx = idx + 1, arr = arr, remain = remain - arr[-1])
                arr.pop()
                curr = candidates[idx]
                
                while len(candidates) > idx and candidates[idx] == curr:
                    idx += 1
                
                recur(idx = idx, arr = arr, remain = remain)
                
            elif remain == candidates[idx]:
                arr.append(candidates[idx])
                answer.add(tuple(arr))
                arr.pop()
                return None
            else:
                return None
        recur(0, [], target)
        return list(answer)
                