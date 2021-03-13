class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def simple_rob(nums: List[int]) -> int:
            rob1 = 0
            rob2 = 0
            for num in nums:
                rob1, rob2 = max(rob2 + num, rob1), rob1
            return rob1
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))
