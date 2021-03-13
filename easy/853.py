class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            n = (l + r) // 2
            if arr[n - 1] < arr[n] and arr[n + 1] < arr[n]:
                return n
            elif arr[n - 1] < arr[n] and arr[n] < arr[n + 1]:
                l = n + 1
            else:
                r = n
        return
