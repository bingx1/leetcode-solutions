class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1 :i + 1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
                    break
        return d[-1]
#memoization array - dp[i] is true only if for some word w; dp[i-len(w)] is true
