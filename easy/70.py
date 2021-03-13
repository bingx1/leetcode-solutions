class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        n1 = 2
        n2 = 1
        for i in range(3, n + 1):
          n1, n2 = n1 + n2, n1
        return n1
    
