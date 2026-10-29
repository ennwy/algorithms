class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # candidates = [2 3 6 7]
        # target = 7
        res = [] # []
        
        def make_combination(idx, comb, total):
            if total == target: 
                res.append(comb[:])
                return
            elif total > target or idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            make_combination(idx, comb, total+candidates[idx])
            comb.pop()
            make_combination(idx+1, comb, total)

        make_combination(0, [], 0)

        return res
    
        
