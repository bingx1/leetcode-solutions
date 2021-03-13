class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.backtrack(res, n, 1, k, [])
        return res
        
    def backtrack(self, res, target, index, k, combo):
        if len(combo) == k:
            if target == 0:
                res.append(combo)
            return
        for i in range(index, 10):
                self.backtrack(res, target - i, i+1, k, combo + [i])
        return
