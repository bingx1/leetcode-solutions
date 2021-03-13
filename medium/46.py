    
class Solution:
    """
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]          
    
    """
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(result, [], nums)
        return result
    
    def backtracking(self, res, subset, nums):
        if len(subset) == len(nums):
            res.append(subset)
            return
        for num in nums:
            if num in subset:
                continue
            self.backtracking(res, subset + [num], nums)
        return
    #warning: involves deep copying of subset - o(n * n!)
