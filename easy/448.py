class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
	x = len(nums) + 1
	for num in nums:
	    nums[(num  % x) - 1] += x
	output = []
	for i in range(len(nums)):
	    if nums[i] < x:
	        output.append(i)
	return output 
