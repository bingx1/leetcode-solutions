class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            current = (lo + hi) //2
            if nums[current] == target:
                return current
            elif nums[current] < target:
                lo = current + 1
            else:
                hi = current - 1
        return -1
