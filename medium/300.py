#basic idea - we want to initialize a memoization array dp, 
# where dp[i] represents the longest subsequence that can be made including
# that number
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0]  * len(nums)
        dp[0] = 1
        longest = 1
        for i in range(1, len(nums)):
            max_val = 0
            
            for j in range(i):
                if nums[i] > nums[j]:
                    max_val = max(max_val, dp[j])
            
            dp[i] = max_val + 1
            longest = max(longest, dp[i])
        return longest

#nlogn solution
#idea - keep track of the best subsequence of each size that can be made
#use binary search to see which tail needs to be updated:
# IF the current number is LESS than the last number of one our tails
# - we're going to need to update the tail with size between 0 
# - and the size of the longest tail we've found so far
# IF the current number is greater than the last number of one of our tails
# - we have found a new tail of size size + 1
# - update tails accordingly


#if the current number is less than the tail,  
class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                # print(m, tails[m], i, j)
                if x > tails[m]:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
            # print(tails[i], tails, size)
        return size
