class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
#         output = [[]]
#         1: output = [[]. [1]]
#         2: output = [[]. [1]. [2]. [1,2]]
#         3: output = [[]. [1], [2]. [1.2]. [3]. [1,3], [2,3], [1,2,3]]
        
        return output
