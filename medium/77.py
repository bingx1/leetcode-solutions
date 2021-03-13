#combinations 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(1, n, k, [], res)
        return res
        
    def backtrack(self, start, n, k, subset, res):
        if len(subset) == k:
            res.append(subset)
        for i in range(start, n+1):
            self.backtrack(i+1, n, k, subset + [i], res)
        return

