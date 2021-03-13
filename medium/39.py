class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtrack(candidates, target, [], res, 0)
        return res 
    
    def backtrack(self, nums, target, combo, res, start):
        if target == 0:
            res.append(combo)
        for i in range(start, len(nums)):
            if nums[i] <= target:
                self.backtrack(nums, target - nums[i], combo + [nums[i]], res, i)
        return
