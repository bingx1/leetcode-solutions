class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        rob1 = 0
        rob2 = 0
        for num in nums:
            rob1, rob2 = max(rob2 + num, rob1), rob1
        return rob1
