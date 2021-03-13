#unique permutations - need a counter - DON'T NEED TO SORT!
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res = []
        self.backtracking(res, counter, [], nums)
        return res
    
    def backtracking(self,res, counter, subset, nums):
        if len(subset) == len(nums):
            res.append(subset)
        for num in counter:
            if counter[num] > 0:
                counter[num] -= 1
                self.backtracking(res, counter, subset+[num], nums)
                counter[num] += 1
        return
    
