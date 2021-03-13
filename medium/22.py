class Solution(object):
    def generateParenthesis(self, N):
        res = []
        self.backtrack(res, N)
        return res
    
    def backtrack(self, res, N, S = '', left = 0, right = 0):
        print(S)
        if len(S) == 2 * N:
            res.append(S)
            return
        if left < N:
            self.backtrack(res, N, S+'(', left+1, right)
        if right < left:
            self.backtrack(res, N, S+')', left, right+1)
        return
