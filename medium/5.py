class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            longest = max(self.getPalindrome(s, i, i), self.getPalindrome(s, i, i+1), longest, key=len)
        return longest
    
    def getPalindrome(self, s, left, right):
        output = ""
        while left >=0 and right < len(s):
            if s[left] != s[right]:
                break
            if left == right:
                output = s[left]
            else:
                output = s[left] + output 
                output = output + s[right]
            left -= 1
            right += 1
        return output
#for every index in the string, look for the longest palindrome from that index
