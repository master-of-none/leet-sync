class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(cur, j, target):
            if target == 0:
                res.append(cur.copy())
                return
            
            if target <= 0:
                return
            
            prev = -1

            for i in range(j, len(candidates)):
                if candidates[i] == prev:
                    continue
                
                cur.append(candidates[i])
                backtrack(cur, i+1, target - candidates[i])
                cur.pop()
                prev = candidates[i]
        
        backtrack([], 0, target)

        return res