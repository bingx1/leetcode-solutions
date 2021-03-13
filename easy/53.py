class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
	max_sum = float('-inf')
	curr_sum = 0
	for num in nums:
	    if num >= curr_sum + num:
		curr_sum = num
	    else:
		curr_sum += num
	    max_sum = max(max_sum, curr_sum)
	return max_sum
